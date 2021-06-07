from django.test import SimpleTestCase, TestCase
from common.crypto import decode_jwt
from test_common.request import request_api, login_test_user
from test_common.validator import validate_reply
from test_common.consts import *
from account_service.schemas import *
from account_service import account_manager
from account_service.models import User
from common.crypto import encode_jwt, decode_jwt


class TestAccountManager(TestCase):

	def setUp(self):
		self.test_user = User.objects.create(
			is_staff=False,
			is_superuser=False,
			email=TEST_EMAIL,
			last_login=0,
			create_time=0
		)

	def test_generate_verification_code(self):
		code = account_manager.generate_verification_code(TEST_EMAIL, force_query=True)
		self.assertEqual(code, TEST_VERIFICATION_CODE)
		code = account_manager.generate_verification_code('hoangmaihuy@pku.edu.cn', force_query=True)
		self.assertTrue(len(code), 6)

	def test_get_verification_code_by_email(self):
		code = account_manager.generate_verification_code(TEST_EMAIL)
		self.assertEqual(code, TEST_VERIFICATION_CODE)
		code = account_manager.get_verification_code_by_email(TEST_EMAIL)
		self.assertEqual(code, TEST_VERIFICATION_CODE)
		code = account_manager.get_verification_code_by_email("test@gmail.com")
		self.assertEqual(code, None)

	def test_generate_token(self):
		token = account_manager.generate_token(self.test_user)
		info = decode_jwt(token)
		self.assertEqual(info["user_id"], self.test_user.id)
		self.assertEqual(info["email"], self.test_user.email)

	def test_get_or_create_user_by_email(self):
		user = account_manager.get_or_create_user_by_email(TEST_EMAIL)
		self.assertEqual(user.email, TEST_EMAIL)

	def test_get_user_by_id(self):
		user = account_manager.get_user_by_id(self.test_user.id, force_query=True)
		self.assertEqual(user.id, self.test_user.id)


class TestAccountApi(SimpleTestCase):
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
