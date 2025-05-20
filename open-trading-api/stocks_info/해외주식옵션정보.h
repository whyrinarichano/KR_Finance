/*****************************************************************************
 *  �ؿ� �����ɼ� ���� ���� (fostkcode.mst)
 ****************************************************************************/
typedef struct ST_FOSTKCODE_TBL
{
    char sSrsCd      [  32]; /* �����ڵ�    (UNIQ-KEY)       */
    char    sAutoOrdGnrlYN[  1];    /* �����ڵ��ֹ� ���� ���� ���� */
    char    sAutoOrdTwapYN[  1];    /* �����ڵ��ֹ� TWAP ���� ���� ���� */
    char    sAutoOrdEcnmYN[  1];    /* �����ڵ� ������ǥ �ֹ� ���� ���� ���� */
    char    sExchSubCd    [  2];    /* ���� �ŷ��� �ڵ� 2019.12.27           */
                                    /*  10:ASX    20:BALTIC   30:BMF      40:CBOE   */
                                    /*  50:CME    51:CME_CBOT 52:CME_NYMEX 53:CME_COMEX */
                                    /*  60:EUREX  70:FTX      80:HKEx             */
                                    /*  90:ICE_US 91:ICE_���� 92:ICE_��ǰ 93:ICE_SG */
                                    /*  A0:ISE    B0:ITA      C0:JSE      D0:KCBT   */
                                    /*  E0:LBMA   F0:LME      G0:MDEX     H0:MDX    */
                                    /*  I0:MEFF   J0:NYSE     K0:OSE      L0:SGX    */
                                    /*  M0:SSE    N0:TFEX     O0:TMX      P0:HNX */
    char    sFiller      [  45];    /* �ʷ�                         */
 char sSeriesKrNm  [  50]; /* �����ѱ۸�                   */
 char sExchCd      [  10]; /* �ŷ����ڵ�                   */
 char sMrktCd      [  10]; /* ǰ���ڵ�                     */
 char sClasCd      [   3]; /* ǰ������                     */
                                 /* 1: �����ɼ�                  */
                                 /* 2: �ֽĿɼ� (M)              */
                                 /* 3: �����ɼ�                  */
                                 /* 4: �����ɼ�                  */
                                 /* 5: �ֽĿɼ� (W)              */
 char sDispDesz    [   5]; /* ��� �Ҽ���                  */
 char sCalcDesz    [   5]; /* ��� �Ҽ���                  */
 char sTickSz      [  14]; /* ƽ������                     */
 char sTickVal     [  14]; /* ƽ��ġ                       */
 char sCtrtSz      [  10]; /* ���ũ��                     */
 char sDispDigit   [   4]; /* ����ǥ������                 */
 char sMultiplier  [  10]; /* ȯ��¼�                     */
 char    sSymbol      [   1];    /* �ɼ� ���� C, P               */
 char    sStkPrc      [  20];    /* Strike Price                 */
    char    sUndrInstr   [  10];    /* ���ü����ڵ�                 */
                                    /*   �ؿܼ��� ǰ�� �ڵ�         */
                                    /* �ֽĿɼ��� ��� �ŷ��� �ڵ�  */
                                    /*   ex: NAS, NYS, AMS          */
    char    sUndrAsset   [  32];    /* ���ü�������                 */
                                    /*   �ؿܼ��� �����ڻ� �����ڵ� */
                                    /* �ֽĿɼ��� ��� Ticker �ڵ�  */
                                    /*   AAPL, TSLA                 */
    char    sRefrAsset   [  32];    /* �����ڻ� Index��             */
                                    /*   �����ΰ�� ������          */
                                    /*   �ؿܼ����ΰ�� ���� ���� �����ڵ� */
 char    sIncTickPrc  [  19];    /* ƽ�������ذ�                 */
    char    sIncTickSz   [   5];    /* ƽ�������                   */
    char    sYearMon     [   6];    /* ���                         */
    char    sAtmFlg      [   1];    /* A: ATM, I:ITM, O:OTM         */
    char    sNearFlg     [   1];    /* �ٿ������� 0:������ 1:�ٿ��� */
} FOSTKCODE_TBL;