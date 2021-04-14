from django.test import TestCase, SimpleTestCase
from common.utils import request_api
from common.consts import *
from account_service.consts import *

# Create your tests here.

class TestAccount(SimpleTestCase):
	def setUp(self) -> None:
		pass

	def test_request_auth_code(self):
		result, reply = request_api(AccountServiceApi.REQUEST_AUTH_CODE, data={
			"email": "example@gmail.com"
		})
		self.assertEqual(result, Result.ERROR_INVALID_EMAIL)

		result, reply = request_api(AccountServiceApi.REQUEST_AUTH_CODE, data={
			"email": TEST_EMAIL,
		})
		self.assertEqual(result, Result.SUCCESS)

	def test_login(self):
		result, reply = request_api(AccountServiceApi.LOGIN, data={
			"email": "example@gmail.com",
			"auth_code": TEST_AUTH_CODE,
		})

		self.assertEqual(result, Result.ERROR_AUTHORIZATION)
		result, reply = request_api(AccountServiceApi.REQUEST_AUTH_CODE, data={
			"email": TEST_EMAIL
		})

		self.assertEqual(result, Result.SUCCESS)
		result, reply = request_api(AccountServiceApi.LOGIN, data={
			"email": TEST_EMAIL,
			"auth_code": TEST_AUTH_CODE
		})
		self.assertEqual(result, Result.SUCCESS)