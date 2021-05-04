from django.test import TestCase, SimpleTestCase
from common.utils import request_api
from common.consts import *
from account_service.consts import *
from account_service import account_manager


class TestAccount(SimpleTestCase):
	def setUp(self) -> None:
		pass

	def _login_test_user(self):
		result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
			"email": TEST_EMAIL
		})

		self.assertEqual(result, Result.SUCCESS)
		result, reply = request_api(AccountServiceApi.LOGIN, data={
			"email": TEST_EMAIL,
			"verification_code": TEST_VERIFICATION_CODE
		})
		self.assertEqual(result, Result.SUCCESS)
		token = reply["access_token"]
		return token

	def test_request_verification_code(self):
		result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
			"email": "example@gmail.com"
		})
		self.assertEqual(result, Result.ERROR_INVALID_EMAIL)

		result, reply = request_api(AccountServiceApi.REQUEST_VERIFICATION_CODE, data={
			"email": "1800094810@pku.edu.cn",
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


	def test_get_user_info(self):
		token = self._login_test_user()
		result, reply = request_api(AccountServiceApi.GET_USER_INFO, method="GET", token=token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertEqual(reply["email"], TEST_EMAIL)
