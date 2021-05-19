import requests
from test_common.consts import *


def request_api(url, method="POST", headers=None, data=None, token=None):
	if not headers:
		headers = {}
	if token:
		headers["Authorization"] = "Bearer " + token
	if method == "GET":
		r = requests.get(url, headers=headers, params=data)
	elif method == "POST":
		r = requests.post(url, headers=headers, json=data)
	else:
		return Result.ERROR_BAD_REQUEST, None

	if r.status_code != 200:
		return r.status_code, None
	resp_data = r.json()
	return resp_data["result"], resp_data.get("reply")


def login_test_user():
	result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
		"email": TEST_EMAIL
	})

	result, reply = request_api(AccountServiceApi.LOGIN, data={
		"email": TEST_EMAIL,
		"verification_code": TEST_VERIFICATION_CODE
	})

	token = reply["access_token"]
	return token
