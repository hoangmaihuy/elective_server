import course_service.class_manager
from common.utils import parse_request
from common.validator import is_valid_semester
from common.consts import *
from review_service.schemas import *
from review_service import review_manager
from course_service import course_manager


@parse_request(method="POST", schema=ADD_REVIEW_REQUEST_SCHEMA, login_required=True)
def add_review(request, data):
	course_id = data["course_id"]
	teacher_id = data["teacher_id"]
	semester = data["semester"]
	title = data.get("title", "")
	content = data.get("content", "")
	if not is_valid_semester(semester):
		return Result.ERROR_PARAMS, None

	course_class = course_service.class_manager.get_class(course_id, teacher_id, semester)
	if not course_class:
		return Result.ERROR_CLASS_NOT_EXIST, None

	class_id = course_class.id
	score = {
		"recommend_score": data["recommend_score"],
		"content_score": data["content_score"],
		"work_score": data["work_score"],
		"exam_score": data["exam_score"],
	}
	user_id = data["__auth_info"]["user_id"]

	if not review_manager.create_review(course_id, teacher_id, class_id, title, content, score, user_id):
		return Result.ERROR_SERVER, None

	return Result.SUCCESS, None


@parse_request(method="POST", schema=GET_LATEST_REVIEWS_REQUEST_SCHEMA, login_required=True)
def get_latest_reviews(request, data):
	user_id = data["__auth_info"]["user_id"]
	offset = data["offset"]
	size = data["size"]
	reviews = review_manager.get_latest_reviews(offset, size, user_id)
	return Result.SUCCESS, {
		"reviews": reviews
	}


@parse_request(method="POST", schema=GET_COURSE_REVIEWS_REQUEST_SCHEMA, login_required=True)
def get_course_reviews(request, data):
	user_id = data["__auth_info"]["user_id"]
	course_id = data["course_id"]
	current_page = data["current_page"]
	page_size = data["page_size"]
	offset = (current_page - 1) * page_size
	teacher_id = data.get("teacher_id")
	semester = data.get("semester")
	if semester and not is_valid_semester(semester):
		return Result.ERROR_PARAMS, None
	class_ids = None
	if semester:
		class_ids = course_manager.get_class_ids_by_semester(course_id, semester)
	sorted_by = data.get("sorted_by", "-create_time")

	total, reviews = review_manager.get_course_reviews(course_id, offset, page_size, sorted_by, teacher_id, class_ids, user_id)
	return Result.SUCCESS, {
		"total": total,
		"reviews": reviews
	}


@parse_request(method="POST", schema=INTERACT_REVIEW_REQUEST_SCHEMA, login_required=True)
def interact_review(request, data):
	user_id = data["__auth_info"]["user_id"]
	review_id = data["review_id"]
	action = data["action"]
	review_manager.interact_review(review_id, action, user_id)
	return Result.SUCCESS, None

