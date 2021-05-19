from django.test import SimpleTestCase
from test_common.consts import *
from test_common.request import request_api, login_test_user


class TestCourse(SimpleTestCase):
	def setUp(self) -> None:
		self._token = login_test_user()

	def test_get_teacher_names(self):
		result, reply = request_api(TeacherServiceApi.GET_TEACHER_LIST, method="GET", token=self._token)
		self.assertEqual(result, Result.SUCCESS)

	def test_get_teachers_by_course(self):
		result, reply = request_api(TeacherServiceApi.GET_TEACHERS_BY_COURSE, data={
			"course_id": TEST_COURSE_ID,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
