/*****************************************************************************
 *  �ؿ� ���� ���� ���� (ffcode.mst)
 ****************************************************************************/
typedef struct ST_FFCODE_TBL
{
	char sSrsCd [ 32]; /* �����ڵ� */
	char sAutoOrdGnrlYN[ 1]; /* �����ڵ��ֹ� ���� ���� ���� */
	char sAutoOrdTwapYN[ 1]; /* �����ڵ��ֹ� TWAP ���� ���� ���� */
	char sAutoOrdEcnmYN[ 1]; /* �����ڵ� ������ǥ �ֹ� ���� ���� ���� */
	char sFiller [ 47]; /* �ʷ� */
	char sSeriesKrNm [ 50]; /* �����ѱ۸� */
	char sExchCd [ 10]; /* �ŷ����ڵ� (ISAM KEY 1) */
	char sMrktCd [ 10]; /* ǰ���ڵ� (ISAM KEY 2) */
	char sClasCd [ 3]; /* ǰ������ */
	char sDispDesz [ 5]; /* ��� �Ҽ��� */
	char sCalcDesz [ 5]; /* ��� �Ҽ��� */
	char sTickSz [ 14]; /* ƽ������ */
	char sTickVal [ 14]; /* ƽ��ġ */
	char sCtrtSz [ 10]; /* ���ũ�� */
	char sDispDigit [ 4]; /* ����ǥ������ */
	char sMultiplier [ 10]; /* ȯ��¼� */
	char sNearFlg [ 1]; /* �ִٿ������� 0:������ 1:�ִٿ��� */
	char sNearFlgDt [ 1]; /* �ֱٿ������� 0:������ 1:�ֱٿ��� */
	char sSprdYN [ 1]; /* �������忩�� */
	char sSprdLeg1YN [ 1]; /* ��������������� LEG1 ���� Y/N */
	char sExchSubCd [ 2]; /* ���� �ŷ��� �ڵ� */
} FFCODE_TBL;
