from django.test import SimpleTestCase, TestCase
from test_common.request import request_api, login_test_user
from test_common.validator import validate_reply
from test_common.consts import *
from review_service.models import *
from review_service.consts import *
from review_service.schemas import *
from review_service import review_manager
from course_service.models import *
from teacher_service.models import *


class TestReviewManager(TestCase):
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
		self.test_teacher = Teacher.objects.create(
			name='Test teacher',
			recommend_score=4.5,
			work_score=3.5,
			content_score=5,
			exam_score=3,
			review_count=1,
			create_time=0,
		)
		self.test_review = Review.objects.create(
			course_id=self.test_course.id,
			teacher_id=self.test_teacher.id,
			class_id=self.test_class.id,
			title="Test review title",
			content="Test review content",
			recommend_score=4,
			work_score=3,
			content_score=2,
			exam_score=1,
			create_by=self.test_user_id,
			create_time=0,
		)

	def test_create_review(self):
		is_success = review_manager.create_review(
			self.test_course.id,
			self.test_teacher.id,
			self.test_class.id,
			title='Test review',
			content='Test content',
			score={
				"recommend_score": 4,
				"content_score": 3,
				"work_score": 3.5,
				"exam_score": 5,
			},
			create_by=0
		)
		self.assertTrue(is_success)

	def test_get_latest_reviews(self):
		total, reviews = review_manager.get_latest_reviews(0, 1, 1, force_query=True)
		self.assertEqual(total, 1)

	def test_get_course_reviews(self):
		total, reviews = review_manager.get_course_reviews(self.test_course.id, 0, 1, "-create_time", user_id=self.test_user_id)
		self.assertEqual(total, 1)
		self.assertTrue(reviews[0]["course_id"], self.test_course.id)

	def test_get_teacher_reviews(self):
		total, reviews = review_manager.get_teacher_reviews(self.test_teacher.id, 0, 1, user_id=self.test_user_id)
		self.assertEqual(total, 1)
		self.assertTrue(reviews[0]["teacher_id"], self.test_teacher.id)

	def test_interact_review(self):
		review_manager.interact_review(self.test_review.id, ReviewInteraction.LIKE, user_id=self.test_user_id)
		interact = ReviewInteract.objects.filter(review_id=self.test_review.id, create_by=self.test_user_id).first()
		self.assertTrue(interact is not None)
		self.assertEqual(interact.action, ReviewInteraction.LIKE)


class TestReviewApi(SimpleTestCase):
	def setUp(self) -> None:
		self._token = login_test_user()

	def test_add_review(self):
		result, _ = request_api(ReviewServiceApi.ADD_REVIEW, data={
			"course_id": TEST_COURSE_ID,
			"teacher_id": TEST_TEACHER_ID,
			"semester": TEST_SEMESTER,
			"title": "Test title",
			"content": "Test content",
			"recommend_score": 4.5,
			"content_score": 4,
			"work_score": 3.5,
			"exam_score": 5,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)

	def test_get_latest_reviews(self):
		result, reply = request_api(ReviewServiceApi.GET_LATEST_REVIEWS, data={
			"offset": 0,
			"size": 10,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_LATEST_REVIEWS_REPLY_SCHEMA))
		# Make sure reviews are sorted by time
		reviews = reply["reviews"]
		for i in range(len(reviews)-1):
			self.assertTrue(reviews[i]["create_time"] >= reviews[i+1]["create_time"])

	def test_get_course_reviews(self):
		result, reply = request_api(ReviewServiceApi.GET_COURSE_REVIEWS, data={
			"course_id": TEST_COURSE_ID,
			"current_page": 1,
			"page_size": 10,
			"semester": TEST_SEMESTER,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_COURSE_REVIEWS_REPLY_SCHEMA))
		# Check if all reviews belong to requested course
		for review in reply["reviews"]:
			self.assertEqual(review["course_id"], TEST_COURSE_ID)

	def test_get_teacher_reviews(self):
		result, reply = request_api(ReviewServiceApi.GET_TEACHER_REVIEWS, data={
			"teacher_id": TEST_TEACHER_ID,
			"current_page": 1,
			"page_size": 10,
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
		self.assertTrue(validate_reply(reply, GET_TEACHER_REVIEWS_REPLY_SCHEMA))
		# Check if all reviews belong to requested course
		for review in reply["reviews"]:
			self.assertEqual(review["teacher_id"], TEST_TEACHER_ID)

	def test_interact_review(self):
		result, reply = request_api(ReviewServiceApi.INTERACT_REVIEW, data={
			"review_id": TEST_REVIEW_ID,
			"action": ReviewInteraction.LIKE
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)

		result, reply = request_api(ReviewServiceApi.INTERACT_REVIEW, data={
			"review_id": TEST_REVIEW_ID,
			"action": ReviewInteraction.DISLIKE
		}, token=self._token)
		self.assertEqual(result, Result.SUCCESS)
