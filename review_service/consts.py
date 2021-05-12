from tuike_api.settings import HOST

REVIEW_SERVICE_API = HOST + "/review"


class ReviewServiceApi:
	ADD_REVIEW = REVIEW_SERVICE_API + "/add_review"


TEST_COURSE_ID = 1824
TEST_TEACHER_ID = 3241
TEST_SEMESTER = "20-21-2"