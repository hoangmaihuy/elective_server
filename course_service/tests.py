from django.test import SimpleTestCase
from common.utils import request_api
from common.consts import *
from course_service.consts import *
from account_service.consts import *


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

	def test_get_course_list(self):
		result, reply = request_api(CourseServiceApi.GET_COURSE_LIST, data={
			"current_page": 1,
			"page_size": 20,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)

	def test_get_courses_by_school(self):
		result, reply = request_api(CourseServiceApi.GET_COURSES_BY_SCHOOL, data={
			"school_ids": [1, 2, 3, 4, 5]
		}, token=self._token)

		self.assertEqual(result, Result.SUCCESS)
