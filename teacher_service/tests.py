from django.test import SimpleTestCase, TestCase
from test_common.consts import *
from test_common.request import request_api, login_test_user
from test_common.validator import validate_reply
from teacher_service.schemas import *
from teacher_service.models import *
from teacher_service import teacher_manager
from course_service.models import *


class TestTeacherManager(TestCase):
	def setUp(self) -> None:
		self.test_user_id = 1
		self.test_school = 1
		self.test_course_type = 100
		self.test_teacher_id = 1
		self.test_semester = '20-21-2'
		self.test_course = Course.objects.create(
			name='Test Course 1',
			course_no='123456',
			credit=2,
			school_id=self.test_school,
			type=self.test_course_type,
			recommend_score=4,
			work_score=4,
			content_score=4,
			exam_score=3,
			review_count=1,
			last_review=0,
			create_time=0,
		)

		self.test_teacher = Teacher.objects.create(
			name='Test teacher',
			recommend_score=4.5,
			work_score=3.5,
			content_score=5,
			exam_score=3,
			review_count=1,
			create_time=0,
		)
		self.test_class = Class.objects.create(
			course_id=self.test_course.id,
			teacher_id=self.test_teacher.id,
			semester=self.test_semester,
			recommend_score=4,
			work_score=3,
			content_score=2,
			exam_score=1,
			review_count=1,
			create_time=0,
		)

	def test_get_teacher_names(self):
		teacher_names = teacher_manager.get_teacher_names(force_query=True)
		self.assertEqual(len(teacher_names), 1)
		self.assertEqual(teacher_names[0]["name"], self.test_teacher.name)

	def test_get_teachers_by_courses(self):
		teachers = teacher_manager.get_teachers_by_course(self.test_course.id, force_query=True)
		self.assertEqual(len(teachers), 1)
		self.assertEqual(teachers[0]["name"], self.test_teacher.name)

	def test_get_teacher_infos_by_ids(self):
		teachers = teacher_manager.get_teacher_infos_by_ids([self.test_teacher.id])
		self.assertEqual(len(teachers), 1)
		self.assertEqual(teachers[0]["name"], self.test_teacher.name)

	def test_get_teacher_info_by_id(self):
		teacher = teacher_manager.get_teacher_info_by_id(self.test_teacher.id)
		self.assertEqual(teacher["name"], self.test_teacher.name)

	def test_update_teacher_score(self):
		old_score = {
			"recommend_score": self.test_teacher.recommend_score,
			"content_score": self.test_teacher.content_score,
			"work_score": self.test_teacher.work_score,
			"exam_score": self.test_teacher.exam_score,
		}
		new_score = {
			"recommend_score": 5,
			"content_score": 3,
			"work_score": 4,
			"exam_score": 3,
		}

		is_success = teacher_manager.update_teacher_score(self.test_teacher.id, new_score)
		self.assertTrue(is_success)
		new_teacher = Teacher.objects.get(id=self.test_teacher.id)
		self.assertEqual(new_teacher.review_count, 2)
		self.assertEqual(new_teacher.recommend_score, (old_score["recommend_score"] + new_score["recommend_score"]) / 2)
		self.assertEqual(new_teacher.content_score, (old_score["content_score"] + new_score["content_score"]) / 2)
		self.assertEqual(new_teacher.work_score, (old_score["work_score"] + new_score["work_score"]) / 2)
		self.assertEqual(new_teacher.exam_score, (old_score["exam_score"] + new_score["exam_score"]) / 2)


class TestTeacherApi(SimpleTestCase):
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
