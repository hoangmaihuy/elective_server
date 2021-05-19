from django.test import SimpleTestCase
from test_common.request import request_api
from common.consts import Result
from test_service.consts import Api as TestServiceApi


class TestService(SimpleTestCase):
	def setUp(self) -> None:
		pass

	def test_echo(self):
		result, reply = request_api(TestServiceApi.ECHO, data={
			"message": "Hello World"
		})

		self.assertEqual(result, Result.SUCCESS)

		self.assertEqual(reply["message"], "Hello World")
