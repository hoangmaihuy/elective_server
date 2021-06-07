from django.test import SimpleTestCase, TestCase
from test_common.request import request_api, login_test_user
from test_common.consts import *
from test_common.validator import validate_reply
from course_service.schemas import *
from course_service.models import *
from course_service import course_manager, class_manager


class TestCourseManager(TestCase):
	def setUp(self) -> None:
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
		Course.objects.create(
			name='Test Course 2',
			course_no='123456',
			credit=3,
			school_id=self.test_school,
			type=self.test_course_type,
			recommend_score=5,
			work_score=4,
			content_score=2,
			exam_score=3,
			last_review=0,
			create_time=0,
		)
		self.test_class = Class.objects.create(
			course_id=self.test_course.id,
			teacher_id=self.test_teacher_id,
			semester=self.test_semester,
			recommend_score=4,
			work_score=3,
			content_score=2,
			exam_score=1,
			review_count=1,
			create_time=0,
		)

	def test_get_courses_by_params(self):
		total, courses = course_manager.get_courses_by_params({
			'school_id': self.test_school,
		})
		self.assertEqual(total, 2)

	def test_get_courses_by_school(self):
		courses_by_school = course_manager.get_courses_by_school(force_query=True)
		courses = courses_by_school[self.test_school]
		self.assertEqual(len(courses), 2)

	def test_get_course_rank(self):
		course_rank = course_manager.get_course_rank(self.test_course_type, self.test_school, rank_size=2, force_query=True)
		self.assertEqual(len(course_rank), 2)
		self.assertTrue(course_rank[0]["recommend_score"] >= course_rank[1]["recommend_score"])

	def test_get_teacher_ids_by_course_id(self):
		teacher_ids = course_manager.get_teacher_ids_by_course_id(self.test_course.id, force_query=True)
		self.assertEqual(teacher_ids[0], self.test_teacher_id)

	def test_get_course_infos_by_id(self):
		course_info = course_manager.get_course_info(self.test_course.id)
		self.assertEqual(course_info["name"], self.test_course.name)

	def test_update_course_score(self):
		old_score = {
			"recommend_score": self.test_course.recommend_score,
			"content_score": self.test_course.content_score,
			"work_score": self.test_course.work_score,
			"exam_score": self.test_course.exam_score,
		}
		new_score = {
			"recommend_score": 5,
			"content_score": 3,
			"work_score": 4,
			"exam_score": 3,
		}
		is_success = course_manager.update_course_score(self.test_course.id, new_score)
		self.assertTrue(is_success)
		new_course = Course.objects.get(id=self.test_course.id)
		self.assertEqual(new_course.review_count, 2)
		self.assertEqual(new_course.recommend_score, (old_score["recommend_score"] + new_score["recommend_score"]) / 2)
		self.assertEqual(new_course.content_score, (old_score["content_score"] + new_score["content_score"]) / 2)
		self.assertEqual(new_course.work_score, (old_score["work_score"] + new_score["work_score"]) / 2)
		self.assertEqual(new_course.exam_score, (old_score["exam_score"] + new_score["exam_score"]) / 2)

	def test_update_class_score(self):
		old_score = {
			"recommend_score": self.test_class.recommend_score,
			"content_score": self.test_class.content_score,
			"work_score": self.test_class.work_score,
			"exam_score": self.test_class.exam_score,
		}
		new_score = {
			"recommend_score": 5,
			"content_score": 3,
			"work_score": 4,
			"exam_score": 3,
		}
		is_success = class_manager.update_class_score(self.test_class.id, new_score)
		self.assertTrue(is_success)
		new_class = Class.objects.get(id=self.test_class.id)
		self.assertEqual(new_class.review_count, 2)
		self.assertEqual(new_class.recommend_score, (old_score["recommend_score"] + new_score["recommend_score"]) / 2)
		self.assertEqual(new_class.content_score, (old_score["content_score"] + new_score["content_score"]) / 2)
		self.assertEqual(new_class.work_score, (old_score["work_score"] + new_score["work_score"]) / 2)
		self.assertEqual(new_class.exam_score, (old_score["exam_score"] + new_score["exam_score"]) / 2)

	def test_get_class(self):
		_class = class_manager.get_class(self.test_class.course_id, self.test_class.teacher_id, self.test_class.semester)
		self.assertEqual(_class.id, self.test_class.id)

	def test_get_class_infos_by_ids(self):
		classes = class_manager.get_class_infos_by_ids([self.test_class.id])
		self.assertEqual(len(classes), 1)
		self.assertEqual(classes[0]["id"], self.test_class.id)


class TestCourseApi(SimpleTestCase):
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
