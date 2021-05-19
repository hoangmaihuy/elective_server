from django.test import SimpleTestCase
from common.crypto import decode_jwt
from test_common.request import request_api, login_test_user
from test_common.validator import validate_reply
from test_common.consts import *
from account_service.schemas import *

class TestAccount(SimpleTestCase):
	def setUp(self) -> None:
		pass

	def test_request_verification_code(self):
		result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
			"email": "example@gmail.com"
		})
		self.assertEqual(result, Result.ERROR_INVALID_EMAIL)

		result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
			"email": TEST_EMAIL,
		})
		self.assertEqual(result, Result.SUCCESS)

	def test_login(self):
		result, reply = request_api(AccountServiceApi.LOGIN, data={
			"email": "example@gmail.com",
			"verification_code": TEST_VERIFICATION_CODE,
		})
		self.assertEqual(result, Result.ERROR_VERIFICATION_CODE)

		result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
			"email": TEST_EMAIL
		})
		self.assertEqual(result, Result.SUCCESS)

		result, reply = request_api(AccountServiceApi.LOGIN, data={
			"email": TEST_EMAIL,
			"verification_code": TEST_VERIFICATION_CODE
		})
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, LOGIN_REPLY_SCHEMA))
		token = decode_jwt(reply["access_token"])
		self.assertEqual(token["user_id"], TEST_UID)
		self.assertEqual(token["email"], TEST_EMAIL)

	def test_get_user_info(self):
		token = login_test_user()
		result, reply = request_api(AccountServiceApi.GET_USER_INFO, method="GET", token=token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_USER_INFO_REPLY_SCHEMA))
		self.assertEqual(reply["user_id"], TEST_UID)
		self.assertEqual(reply["email"], TEST_EMAIL)
		self.assertEqual(reply["authority"], "user")
