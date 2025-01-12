import requests

BASE_URL = '...' # 도메인 주소
APPKEY = '...' # 발급받은 APPKEY
APPSECRET = '...' # 발급받은 APPSECRET
ACCESS_TOKEN = '...' # get_token.py의 결과값으로 받은 token

url = f'{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice'
headers = {
    'content-type': 'application/json; charset=utf-8',
    'authorization': f'Bearer {ACCESS_TOKEN}',
    'appkey': APPKEY,
    'appsecret': APPSECRET,
    'tr_id': 'FHKST03010200',
    'custtype': 'P'
}
params = {
    'FID_ETC_CLS_CODE': '',
    'FID_COND_MRKT_DIV_CODE': 'J',
    'FID_INPUT_ISCD': '005930',
    'FID_INPUT_HOUR_1': '093000',
    'FID_PW_DATA_INCU_YN': 'Y'
}

try:
    info = [] 
    res = requests.get(url, headers=headers, params=params)
    data = res.json()
    for item in data['output2']: # output2의 item은 사전객체로, 각각 1분봉 정보를 의미함
        info.append(item)     
except Exception as e:
    print(e)

