from django.test import SimpleTestCase
from common.consts import *
from common.utils import *
from account_service.consts import *
from teacher_service.consts import *
from review_service.consts import TEST_COURSE_ID



class TestCourse(SimpleTestCase):
	def setUp(self) -> None:
		self._token = self._login_test_user()

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

	def test_get_teacher_names(self):
		result, reply = request_api(TeacherServiceApi.GET_TEACHER_LIST, method="GET", token=self._token)
		self.assertEqual(result, Result.SUCCESS)

	def test_get_teachers_by_course(self):
		result, reply = request_api(TeacherServiceApi.GET_TEACHERS_BY_COURSE, data={
			"course_id": TEST_COURSE_ID,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		print(reply)
