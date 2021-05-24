from django.test import SimpleTestCase
from test_common.request import request_api, login_test_user
from test_common.validator import validate_reply
from test_common.consts import *
from review_service.consts import *
from review_service.schemas import *


class TestReview(SimpleTestCase):
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
