# API DETAILS
END_POINT = 'https://paper-api.alpaca.markets'
API_KEY_ID = 'XXX'
SECRECT_KEY = 'XXX'

# API Endpoints
BASE_URL = END_POINT
ORDERS = '{0}/v2/orders'.format(BASE_URL)
ACCOUNT = '{0}/v2/account'.format(BASE_URL)

# API Header Dict
headers = {"APCA-API-KEY-ID": API_KEY_ID,"APCA-API-SECRET-KEY": SECRECT_KEY}
