/*****************************************************************************
 *  �ڽ��� ���� �ڵ� ���� ����
 ****************************************************************************/
typedef struct
{
    char    mksc_shrn_iscd[SZ_SHRNCODE];        /* �����ڵ�                                     */
    char    stnd_iscd[SZ_STNDCODE];             /* ǥ���ڵ�                                     */
    char    hts_kor_isnm[SZ_KORNAME];           /* �ѱ������                                   */
    char    scrt_grp_cls_code[2];               /* ���Ǳ׷챸���ڵ�                             */
                                                /* ST:�ֱ� MF:��������ȸ�� RT:�ε�������ȸ��    */
                                                /* SC:��������ȸ�� IF:��ȸ�����ں�������ȸ��    */
                                                /* DR:�ֽĿ�Ź���� EW:ELW EF:ETF                */
                                                /* SW:�����μ������� SR:�����μ�������          */
                                                /* BC:�������� FE:�ؿ�ETF FS:�ܱ��ֱ�           */
	char    avls_scal_cls_code[1];              /* �ð��Ѿ� �Ը� ���� �ڵ� ����                 */
												/* (0:���� 1:�� 2:�� 3:��)                      */
    char    bstp_larg_div_code[4];              /* ���� ���� ��з� �ڵ�                        */
    char    bstp_medm_div_code[4];              /* ���� ���� �ߺз� �ڵ�                        */
    char    bstp_smal_div_code[4];              /* ���� ���� �Һз� �ڵ�                        */
    char    mnin_cls_code_yn[1];                /* ������ ���� �ڵ� (Y/N)                       */
    char    low_current_yn[1];               	/* ������������ ���� 							*/
    char    sprn_strr_nmix_issu_yn[1];          /* ���� ���� ���� ���� ���� (Y/N)               */
    char    kospi200_apnt_cls_code[1];          /* KOSPI200 ���;���(20110401 �����) 			*/
                                                /* 0:�̺з� 1:�Ǽ���� 2:������� 3:ö������ 	*/
												/* 4:������ȭ�� 5:������� 6:���� 7:�ʼ��Һ��� 	*/
												/* 8: �����Һ���                                */
    char    kospi100_issu_yn[1];                /* KOSPI100����                                 */
    char    kospi50_issu_yn[1];                 /* KOSPI50 ���� ����                            */
    char    krx_issu_yn[1];                     /* KRX ���� ����                                */
    char    etp_prod_cls_code[1];            	/* ETP ��ǰ�����ڵ�								*/
												/* 0:�ش���� 1:����ȸ���� 2:����������			*/
												/* 3:ETN 4:�ս�����ETN							*/
    char    elw_pblc_yn[1];                     /* ELW ���࿩�� (Y/N)                           */
    char    krx100_issu_yn[1];                  /* KRX100 ���� ���� (Y/N)                       */
    char    krx_car_yn[1];                      /* KRX �ڵ��� ����                              */
    char    krx_smcn_yn[1];                     /* KRX �ݵ�ü ����                              */
    char    krx_bio_yn[1];                      /* KRX ���̿� ����                              */
    char    krx_bank_yn[1];                     /* KRX ���� ����                                */
    char    etpr_undt_objt_co_yn[1];            /* ����μ�����ȸ�翩�� 						*/
    char    krx_enrg_chms_yn[1];                /* KRX ������ ȭ�� ����                         */
    char    krx_stel_yn[1];                     /* KRX ö�� ����                                */
    char    short_over_cls_code[1];             /* �ܱ�������񱸺��ڵ� 0:�ش����              */
                                                /* 1:�������� 2:���� 3:��������(��������)       */
    char    krx_medi_cmnc_yn[1];                /* KRX �̵�� ��� ����                         */
    char    krx_cnst_yn[1];                     /* KRX �Ǽ� ����                                */
    char    krx_fnnc_svc_yn[1];                 /* ������(20151218)								*/
    char    krx_scrt_yn [1];                    /* KRX ���� ����                                */
    char    krx_ship_yn [1];                    /* KRX ���� ����                                */
    char    krx_insu_yn[1];                     /* KRX�������� ���迩��                         */
    char    krx_trnp_yn[1];                     /* KRX�������� ��ۿ���                         */
	char	sri_nmix_yn[1];                     /* SRI �������� (Y,N)                           */
	char    stck_sdpr[9];                       /* �ֽ� ���ذ�                                  */
    char    frml_mrkt_deal_qty_unit[5];         /* ���� ���� �Ÿ� ���� ����                     */
    char    ovtm_mrkt_deal_qty_unit[5];         /* �ð��� ���� �Ÿ� ���� ����                   */
    char    trht_yn[1];                         /* �ŷ����� ����                                */
    char    sltr_yn[1];                         /* �����Ÿ� ����                                */
    char    mang_issu_yn[1];                    /* ���� ���� ����                               */
    char    mrkt_alrm_cls_code[2];              /* ���� ��� ���� �ڵ� (00:�ش���� 01:�������� */
                                                /* 02:���ڰ�� 03:��������                      */
	char    mrkt_alrm_risk_adnt_yn[1];          /* ���� ������� ���� ����                      */
    char    insn_pbnt_yn[1];                    /* �Ҽ��� ���� ����                             */
    char    byps_lstn_yn[1];                    /* ��ȸ ���� ����                               */
    char    flng_cls_code[2];                   /* ������ �ڵ� (00:�ش���׾��� 01:�Ǹ���       */
                                                /* 02:���� 03:�й�� 04:�ǹ�� 05:�߰�����  */
                                                /* 06:�Ǹ��߰����� 99:��Ÿ                    */
                                                /* S?W,SR,EW�� ���ش�(SPACE)                     */
    char    fcam_mod_cls_code[2];               /* �׸鰡 ���� ���� �ڵ� (00:�ش����           */
                                                /* 01:�׸���� 02:�׸麴�� 99:��Ÿ              */
    char    icic_cls_code[2];                   /* ���� ���� �ڵ� (00:�ش���� 01:��������      */
                                                /* 02:�������� 03:���������� 99:��Ÿ)           */
    char    marg_rate[3];                       /* ���ű� ����                                  */
    char    crdt_able[1];                       /* �ſ��ֹ� ���� ����                           */
    char    crdt_days[3];                       /* �ſ�Ⱓ                                     */
    char    prdy_vol[12];                       /* ���� �ŷ���                                  */
    char    stck_fcam[12];                      /* �ֽ� �׸鰡                                  */
    char    stck_lstn_date[8];                  /* �ֽ� ���� ����                               */
    char    lstn_stcn[15];                      /* ���� �ּ�(õ)                                */
    char    cpfn[21];                           /* �ں���                                       */
    char    stac_month[2];                      /* ��� ��                                      */
    char    po_prc[7];                          /* ���� ����                                    */
    char    prst_cls_code[1];                   /* �켱�� ���� �ڵ� (0:�ش����(������)         */
                                                /* 1:�����켱�� 2:�����켱��                    */
    char    ssts_hot_yn[1];                     /* ���ŵ��������񿩺�  							*/
    char    stange_runup_yn[1];                 /* �̻�޵����񿩺� 							*/
    char    krx300_issu_yn[1];                  /* KRX300 ���� ���� (Y/N)                       */
    char    kospi_issu_yn[1];                   /* KOSPI����                                    */
	char	sale_account[9];					/* �����                                       */
	char    bsop_prfi[9];						/* ��������                                     */
	char	op_prfi[9];							/* �������                                     */
	char	thtr_ntin[5];						/* ��������                                   */
	char	roe[9];								/* ROE(�ڱ��ں����ͷ�)                          */
	char	base_date[8];						/* ���س��                                     */
	char	prdy_avls_scal[9];					/* ���ϱ��� �ð��Ѿ� (��)                       */

	char	grp_code[3];						/* �׷�� �ڵ�                                  */
    char    co_crdt_limt_over_yn[1];            /* ȸ��ſ��ѵ��ʰ�����                         */
    char    secu_lend_able_yn[1];               /* �㺸���Ⱑ�ɿ���                             */
    char    stln_able_yn[1];                    /* ���ְ��ɿ���                                 */
}   ST_KSP_CODE;