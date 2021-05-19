from django.test import SimpleTestCase
from test_common.request import request_api, login_test_user
from test_common.consts import *
from test_common.validator import validate_reply
from course_service.schemas import *


class TestCourse(SimpleTestCase):
	def setUp(self) -> None:
		self._token = login_test_user()

	def test_get_course_list(self):
		result, reply = request_api(CourseServiceApi.GET_COURSE_LIST, data={
			"current_page": 1,
			"page_size": 20,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_COURSE_LIST_REPLY_SCHEMA))

	def test_get_courses_by_school(self):
		result, reply = request_api(CourseServiceApi.GET_COURSES_BY_SCHOOL, method="GET", token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_COURSES_BY_SCHOOL_REPLY_SCHEMA))

	def test_get_course_rank(self):
		result, reply = request_api(CourseServiceApi.GET_COURSE_RANK, method="POST", data={
			"course_type": 100,
			"school_id": 2,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_COURSE_RANK_REPLY_SCHEMA))
		# Make sure courses are sorted descending by score
		courses = reply["courses"]
		for i in range(len(courses)-1):
			self.assertTrue(courses[i]["recommend_score"] >= courses[i+1]["recommend_score"])

	def test_get_course_info(self):
		result, reply = request_api(CourseServiceApi.GET_COURSE_INFO, method="POST", data={
			"course_id": 99999,
		}, token=self._token)
		self.assertEqual(result, Result.ERROR_COURSE_NOT_FOUND)

		result, reply = request_api(CourseServiceApi.GET_COURSE_INFO, method="POST", data={
			"course_id": TEST_COURSE_ID,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_COURSE_INFO_REPLY_SCHEMA))
		self.assertEqual(reply["id"], TEST_COURSE_ID)
