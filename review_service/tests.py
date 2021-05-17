from django.test import SimpleTestCase
from common.utils import request_api
from common.consts import *
from review_service.consts import *
from account_service.consts import *


class TestReview(SimpleTestCase):
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