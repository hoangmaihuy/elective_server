from tuike_api.settings import HOST

ACCOUNT_SERVICE_API = HOST + "/account"


class AccountServiceApi:
	REQUEST_AUTH_CODE = ACCOUNT_SERVICE_API + "/request_auth_code"
	LOGIN = ACCOUNT_SERVICE_API + "/login"
	LOGOUT = ACCOUNT_SERVICE_API + "/logout"

TEST_EMAIL = 'test@pku.edu.cn'
TEST_AUTH_CODE = '123456'

AUTH_CODE_CACHE_PREFIX = "AUTH_CODE"
AUTH_CODE_CACHE_TIMEOUT = 60 * 5