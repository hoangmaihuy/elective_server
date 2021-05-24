from django.test import SimpleTestCase
from test_common.consts import *
from test_common.request import request_api, login_test_user
from test_common.validator import validate_reply
from teacher_service.schemas import *


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
		self.assertTrue(validate_reply(reply, GET_TEACHERS_BY_COURSE_REPLY_SCHEMA))

	def test_get_teacher_info(self):
		result, reply = request_api(TeacherServiceApi.GET_TEACHER_INFO, data={
			"teacher_id": TEST_TEACHER_ID,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_TEACHER_INFO_REPLY_SCHEMA))
