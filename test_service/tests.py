from django.test import TestCase
from common.utils import request_api
from common.consts import ErrorCode
from test_service.consts import Api as TestServiceApi


class TestService(TestCase):
	def setUp(self) -> None:
		pass

	def test_echo(self):
		err, reply = request_api(TestServiceApi.ECHO, data={
			"message": "Hello World"
		})

		assert(err == ErrorCode.OK)
		assert(reply["message"] == "Hello World")
