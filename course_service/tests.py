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
		result, reply = request_api(CourseServiceApi.GET_COURSES_BY_SCHOOL, method="GET", token=self._token)
		self.assertEqual(result, Result.SUCCESS)

	def test_get_course_rank(self):
		result, reply = request_api(CourseServiceApi.GET_COURSE_RANK, method="POST", data={
			"course_type": 100,
			"school_id": 2,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)

	def test_get_course_info(self):
		result, reply = request_api(CourseServiceApi.GET_COURSE_INFO, method="POST", data={
			"course_id": 99999,
		}, token=self._token)
		self.assertEqual(result, Result.ERROR_COURSE_NOT_FOUND)

		result, reply = request_api(CourseServiceApi.GET_COURSE_INFO, method="POST", data={
			"course_id": 1,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
