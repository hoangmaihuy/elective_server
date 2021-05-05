from common.utils import parse_request
from common.consts import *
from course_service.schemas import *
from course_service import course_manager


@parse_request(method="POST", schema=GET_COURSE_LIST_SCHEMA, auth_required=True)
def get_course_list(request, data):
	current_page = data["current_page"]
	page_size = data["page_size"]
	offset = (current_page-1) * page_size
	total, courses = course_manager.get_all_courses(offset, page_size)
	return Result.SUCCESS, {
		"total": total,
		"courses": courses
	}