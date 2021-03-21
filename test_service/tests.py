from django.test import TestCase
from common.utils import request_api
from common.consts import Result
from test_service.consts import Api as TestServiceApi


class TestService(TestCase):
	def setUp(self) -> None:
		pass

	def test_echo(self):
		result, reply = request_api(TestServiceApi.ECHO, data={
			"message": "Hello World"
		})

		self.assertEqual(result, Result.SUCCESS)

		self.assertEqual(reply["message"], "Hello World")
