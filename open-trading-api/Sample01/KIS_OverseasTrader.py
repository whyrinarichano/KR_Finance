# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:57:19 2023

@author: Administrator
"""
import kis_auth as kis

import time, copy
import requests
import json

import pandas as pd

from collections import namedtuple
from datetime import datetime
from pandas import DataFrame

class KISOverseasTrader:
    def __init__(self, is_mock: bool = True, product: str = '01'):
        svr = 'vps' if is_mock else 'prod'
        self.token_key = kis.read_token()
        kis.changeTREnv(self.token_key, svr=svr, product=product)
        self.env = kis.getTREnv()

        self.account = self.env.my_acct
        self.product_code = self.env.my_prod
        self.token = self.env.my_token
        self.base_url = self.env.my_url
        self.is_mock = is_mock

    def _request_api(self, url, tr_id, params, post=False, tr_cont=""):
        res = kis._url_fetch(url, tr_id, tr_cont, params, postFlag=post)
        
        if str(res.getBody().rt_cd) == "0":
            body = res.getBody()
            if hasattr(body, "output"):
                return pd.DataFrame(body.output if isinstance(body.output, list) else [body.output])
            elif hasattr(body, "output1"):
                return pd.DataFrame(body.output1)
            elif hasattr(body, "output2"):
                return pd.DataFrame(body.output2)
            elif hasattr(body, "output3"):
                return pd.DataFrame(body.output3)
        else:
            print(f"[ERROR] {res.getBody().msg_cd} - {res.getBody().msg1}")
            return None

    def get_overseas_order(self, ord_dv, excg_cd, itm_no, qty, unpr):
        url = '/uapi/overseas-stock/v1/trading/order'
        tr_id = {
            ('buy', True): "TTTT1002U",
            ('sell', True): "TTTT1006U",
            ('buy', False): "TTTT1001U",
            ('sell', False): "TTTT1005U"
        }.get((ord_dv, self.is_mock), None)
        if not tr_id:
            raise ValueError("Invalid order direction or exchange code")

        params = {
            "CANO": self.account,
            "ACNT_PRDT_CD": self.product_code,
            "OVRS_EXCG_CD": excg_cd,
            "PDNO": itm_no,
            "ORD_DVSN": "00",
            "ORD_QTY": str(qty),
            "OVRS_ORD_UNPR": str(unpr),
            "SLL_TYPE": "" if ord_dv == "buy" else "00",
            "ORD_SVR_DVSN_CD": "0"
        }
        return self._request_api(url, tr_id, params, post=True)

    def get_overseas_order_rvsecncl(self, excg_cd, itm_no, orgn_odno, rvse_cncl_dvsn_cd, qty, unpr):
        url = '/uapi/overseas-stock/v1/trading/order-rvsecncl'
        tr_id = "TTTT1004U" if self.is_mock else "TTTT1003U"
        params = {
            "CANO": self.account,
            "ACNT_PRDT_CD": self.product_code,
            "OVRS_EXCG_CD": excg_cd,
            "PDNO": itm_no,
            "ORGN_ODNO": orgn_odno,
            "RVSE_CNCL_DVSN_CD": rvse_cncl_dvsn_cd,
            "ORD_QTY": str(qty),
            "OVRS_ORD_UNPR": str(unpr),
            "MGCO_APTM_ODNO": "",
            "ORD_SVR_DVSN_CD": "0"
        }
        return self._request_api(url, tr_id, params, post=True)

    def get_overseas_order_allcncl(self, excg_cd):
        url = '/uapi/overseas-stock/v1/trading/inquire-nccs'
        tr_id = "TTTS3018R"
        FK100 = NK100 = ""
        dataframe = None
        while True:
            params = {
                "CANO": self.account,
                "ACNT_PRDT_CD": self.product_code,
                "OVRS_EXCG_CD": excg_cd,
                "SORT_SQN": "DS",
                "CTX_AREA_FK200": FK100,
                "CTX_AREA_NK200": NK100
            }
            res = kis._url_fetch(url, tr_id, "", params)
            current = pd.DataFrame(res.getBody().output)
            dataframe = pd.concat([dataframe, current], ignore_index=True) if dataframe is not None else current

            tr_cont = res.getHeader().tr_cont
            FK100, NK100 = res.getBody().ctx_area_fk200, res.getBody().ctx_area_nk200
            if tr_cont in ("D", "E"):
                break
            time.sleep(0.1)
        return dataframe

    def get_overseas_inquire_balance(self, excg_cd="NASD", crcy_cd="USD"):
        url = '/uapi/overseas-stock/v1/trading/inquire-balance'
        tr_id = 'VTTS3012R' if self.is_mock else 'TTTS3012R'
        params = {
            "CANO": self.account,
            "ACNT_PRDT_CD": self.product_code,
            "OVRS_EXCG_CD": excg_cd,
            "TR_CRCY_CD": crcy_cd,
            "CTX_AREA_FK200": "",
            "CTX_AREA_NK200": ""
        }
        print(params)
        print(url, tr_id)
        return self._request_api(url, tr_id, params)
    
    def get_overseas_inquire_nccs(excg_cd="", tr_cont="", FK100="", NK100="", dataframe=None):
        url = '/uapi/overseas-stock/v1/trading/inquire-nccs'
        
        tr_id = 'VTTS3018R' if self.is_mock else 'TTTS3018R'

        t_cnt = 0

        if excg_cd == "": # 해외거래소코드 필수
            print("해외거래소코드 확인요망!!!")
            return None

        params = {
            "CANO": kis.getTREnv().my_acct,         # 종합계좌번호 8자리
            "ACNT_PRDT_CD": kis.getTREnv().my_prod, # 계좌상품코드 2자리
            "OVRS_EXCG_CD": excg_cd,                # 해외거래소코드 NASD:나스닥,NYSE:뉴욕,AMEX:아멕스,SEHK:홍콩,SHAA:중국상해,SZAA:중국심천,TKSE:일본,HASE:베트남하노이,VNSE:호치민
            "SORT_SQN": "DS",                       # DS : 정순, 그외 : 역순
            "CTX_AREA_FK200": FK100,                # 공란 : 최초 조회시 이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)
            "CTX_AREA_NK200": NK100                 # 공란 : 최초 조회시 이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)
        }

        res = kis._url_fetch(url, tr_id, tr_cont, params)

        # Assuming 'output' is a dictionary that you want to convert to a DataFrame
        # current_data = res.getBody().output  # getBody() kis_auth.py 존재
        current_data = pd.DataFrame(res.getBody().output)

        # Append to the existing DataFrame if it exists
        if dataframe is not None:
            dataframe = pd.concat([dataframe, current_data], ignore_index=True)  #
        else:
            dataframe = current_data

        tr_cont, FK100, NK100 = res.getHeader().tr_cont, res.getBody().ctx_area_fk200, res.getBody().ctx_area_nk200 # 페이징 처리 getHeader(), getBody() kis_auth.py 존재
        print(tr_cont, FK100, NK100)

        if tr_cont == "D" or tr_cont == "E": # 마지막 페이지
            print("The End")
            current_data = pd.DataFrame(dataframe)
            cnt = current_data.count()

            # Initialize t_cnt if not already initialized
            try:
                t_cnt += cnt
            except NameError:
                t_cnt = cnt

            if t_cnt.empty:
                print("미체결내역 없음")
            else:
                print("미체결내역 있음")

            dataframe = current_data
            return dataframe
        elif tr_cont == "F" or tr_cont == "M": # 다음 페이지 존재하는 경우 자기 호출 처리
            print('Call Next')
            time.sleep(0.1)  # 시스템 안정적 운영을 위하여 반드시 지연 time 필요
            return get_overseas_inquire_nccs(excg_cd, "N", FK100, NK100, dataframe)
    def get_overseas_inquire_ccnl(st_dt="", ed_dt="", ord_dv="00", ccld_dv="00", excg_cd="%", tr_cont="", FK100="", NK100="", dataframe=None):
        url = '/uapi/overseas-stock/v1/trading/inquire-ccnl'
        tr_id = 'VTTS3035R' if self.is_mock else 'TTTS3035R'

        t_cnt = 0

        if st_dt =="":
            st_dt = datetime.today().strftime("%Y%m%d")   # 주문내역조회 시작일자 값이 없으면 현재일자

        if ed_dt =="":
            ed_dt = datetime.today().strftime("%Y%m%d")   # 주문내역조회 종료일자 값이 없으면 현재일자

        params = {
            "CANO": kis.getTREnv().my_acct,         # 종합계좌번호 8자리
            "ACNT_PRDT_CD": kis.getTREnv().my_prod, # 계좌상품코드 2자리
            "PDNO": "%",                            # 전종목일 경우 "%" 입력  ※ 모의투자계좌의 경우 ""(전체 조회)만 가능
            "ORD_STRT_DT": st_dt,                   # YYYYMMDD 형식 (현지시각 기준)
            "ORD_END_DT": ed_dt,                    # YYYYMMDD 형식 (현지시각 기준)
            "SLL_BUY_DVSN": ord_dv,                 # 매도매수구분 00:전체,01:매도,02:매수   ※ 모의투자계좌의 경우 "00"(전체 조회)만 가능
            "CCLD_NCCS_DVSN": ccld_dv,              # 체결미체결구분 00:전체,01:체결,02:미체결 ※ 모의투자계좌의 경우 "00"(전체 조회)만 가능
            "OVRS_EXCG_CD": excg_cd,                # 해외거래소코드, 전종목일 경우 "%" 입력, NASD:미국시장 전체(나스닥,뉴욕,아멕스),NYSE:뉴욕,AMEX:아멕스,SEHK:홍콩,SHAA:중국상해,SZAA:중국심천,TKSE:일본,HASE:베트남하노이,VNSE:호치민
            "SORT_SQN": "DS",                       # DS:정순,AS:역순, ※ 모의투자계좌의 경우 정렬순서 사용불가(Default : DS(정순))
            "ORD_DT": "",                           # "" (Null 값 설정)
            "ORD_GNO_BRNO": "",                     # "" (Null 값 설정)
            "ODNO": "",                             # "" (Null 값 설정)
            "CTX_AREA_FK200": FK100,                # 공란 : 최초 조회시 이전 조회 Output CTX_AREA_FK100 값 : 다음페이지 조회시(2번째부터)
            "CTX_AREA_NK200": NK100                 # 공란 : 최초 조회시 이전 조회 Output CTX_AREA_NK100 값 : 다음페이지 조회시(2번째부터)
        }

        res = kis._url_fetch(url, tr_id, tr_cont, params)

        # Assuming 'output' is a dictionary that you want to convert to a DataFrame
        # current_data = res.getBody().output  # getBody() kis_auth.py 존재
        current_data = pd.DataFrame(res.getBody().output)

        # Append to the existing DataFrame if it exists
        if dataframe is not None:
            dataframe = pd.concat([dataframe, current_data], ignore_index=True)  #
        else:
            dataframe = current_data

        tr_cont, FK100, NK100 = res.getHeader().tr_cont, res.getBody().ctx_area_fk200, res.getBody().ctx_area_nk200 # 페이징 처리 getHeader(), getBody() kis_auth.py 존재
        #print(tr_cont, FK100, NK100)

        if tr_cont == "D" or tr_cont == "E": # 마지막 페이지
            print("The End")
            current_data = pd.DataFrame(dataframe)
            cnt = current_data.count()

            # Initialize t_cnt if not already initialized
            try:
                t_cnt += cnt
            except NameError:
                t_cnt = cnt

            if t_cnt.empty:
                print("잔고내역 없음")
            else:
                print("잔고내역 있음")

            dataframe = current_data
            return dataframe
        elif tr_cont == "F" or tr_cont == "M": # 다음 페이지 존재하는 경우 자기 호출 처리
            print('Call Next')
            time.sleep(0.1)  # 시스템 안정적 운영을 위하여 반드시 지연 time 필요
            return get_overseas_inquire_ccnl(st_dt, ed_dt, ord_dv, ccld_dv, excg_cd, "N", FK100, NK100, dataframe)

    def get_overseas_inquire_psamount(dv="03", dvsn="01", natn="000", mkt="00", inqr_dvsn="00", tr_cont="", FK100="", NK100="", dataframe=None):
        url = '/uapi/overseas-stock/v1/trading/inquire-psamount'
        
        tr_id = 'VTTS3007R' if self.is_mock else 'TTTS3007R'

        t_cnt = 0

        params = {
            "CANO": kis.getTREnv().my_acct,         # 종합계좌번호 8자리
            "ACNT_PRDT_CD": kis.getTREnv().my_prod, # 계좌상품코드 2자리
            "OVRS_EXCG_CD": dvsn,              # 원화외화구분코드 01 : 원화, 02 : 외화
            "OVRS_ORD_UNPR": natn,                        # 국가코드 000 전체, 840 미국, 344 홍콩, 156 중국, 392 일본, 704 베트남
            "ITEM_CD": inqr_dvsn               # 00 : 전체,01 : 일반해외주식,02 : 미니스탁
        }

        res = kis._url_fetch(url, tr_id, tr_cont, params)

        if str(res.getBody().rt_cd) == "0":
            current_data = pd.DataFrame(res.getBody().output, index=[0])
            dataframe = current_data
        else:
            print(res.getBody().msg_cd + "," + res.getBody().msg1)
            #print(res.getErrorCode() + "," + res.getErrorMessage())
            dataframe = None

        return dataframe
    def get_overseas_daytime_order(ord_dv="", excg_cd="", itm_no="", qty=0, unpr=0, tr_cont="", FK100="", NK100="", dataframe=None):  # 국내주식주문 > 주식주문(현금)
        url = '/uapi/overseas-stock/v1/trading/daytime-order'

        if ord_dv == "buy":
            tr_id = "TTTS6036U"  # 미국주간매수
        elif ord_dv == "sell":
            tr_id = "TTTS6037U"  # 미국주간매도
        else:
            print("매수매도구분(ord_dv) 확인요망!!!")
            return None

        if excg_cd == "":
            print("해외거래소코드(excg_cd) 확인요망!!!")
            return None

        if itm_no == "":
            print("주문종목번호(itm_no 상품번호) 확인요망!!!")
            return None

        if qty == 0:
            print("주문수량(qty) 확인요망!!!")
            return None

        if unpr == 0:
            print("해외주문단가(unpr) 확인요망!!!")
            return None

        params = {
            "CANO": kis.getTREnv().my_acct,         # 종합계좌번호 8자리
            "ACNT_PRDT_CD": kis.getTREnv().my_prod, # 계좌상품코드 2자리
            "OVRS_EXCG_CD": excg_cd,                # 해외거래소코드 NASD:나스닥,NYSE:뉴욕,AMEX:아멕스
            "PDNO": itm_no,                         # 종목코드
            "ORD_DVSN": "00",                       # 주문구분 00:지정가 * 주간거래는 지정가만 가능
            "ORD_QTY": str(int(qty)),               # 주문주식수
            "OVRS_ORD_UNPR": str(int(unpr)),        # 해외주문단가
            "CTAC_TLNO": "",                        # 연락전화번호
            "MGCO_APTM_ODNO": "",                   # 운용사지정주문번호
            "ORD_SVR_DVSN_CD": "0"                  # 주문서버구분코드
        }

        res = kis._url_fetch(url, tr_id, tr_cont, params, postFlag=True)
        if str(res.getBody().rt_cd) == "0":
            current_data = pd.DataFrame(res.getBody().output, index=[0])
            dataframe = current_data
        else:
            print(res.getBody().msg_cd + "," + res.getBody().msg1)
            #print(res.getErrorCode() + "," + res.getErrorMessage())
            dataframe = None

        return dataframe
    # 이하 함수들은 동일한 패턴을 따라 구현하되,
    # 각 API 별로 tr_id 및 url, 필수 파라미터는 맞게 설정하면 됩니다.
    # 예:  
    #  get_overseas_daytime_order_rvsecncl(),
    # get_overseas_inquire_period_profit(), get_overseas_inquire_foreign_margin(),
    # get_overseas_inquire_period_trans(), get_overseas_inquire_paymt_stdr_balance() 등

    # 필요한 추가 메서드들을 요청하시면 이어서 작성해드릴 수 있습니다.
