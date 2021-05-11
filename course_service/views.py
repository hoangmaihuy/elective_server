from common.utils import parse_request
from common.consts import *
from course_service.schemas import *
from course_service.consts import *
from course_service import course_manager


@parse_request(method="POST", schema=GET_COURSE_LIST_SCHEMA, login_required=True)
def get_course_list(request, data):
	current_page = data["current_page"]
	page_size = data["page_size"]
	course_name = data.get("course_name")
	course_no = data.get("course_no")
	course_type = data.get("course_type")
	school_id = data.get("school_id")
	order_by = data.get("order_by")
	offset = (current_page-1) * page_size

	params = {}
	if course_name:
		params["name__contains"] = course_name
	if course_no:
		params["course_no__contains"] = course_no
	if school_id:
		params["school_id"] = school_id
	if course_type:
		if course_type % 100 == 0:
			params["type__range"] = (course_type, course_type + 99)
		else:
			params["type"] = course_type
	if order_by is None:
		order_by = "-review_count"

	total, courses = course_manager.get_courses_by_params(params, order_by, offset, page_size)
	return Result.SUCCESS, {
		"total": total,
		"courses": courses
	}


@parse_request(method="POST", schema=GET_COURSES_BY_SCHOOL, login_required=True)
def get_courses_by_school(request, data):
	school_ids = data["school_ids"]
	for school_id in school_ids:
		if school_id not in SchoolEnum.values():
			return Result.ERROR_PARAMS, None

	courses = course_manager.get_courses_by_school_ids(school_ids)
	courses_by_school = {}
	for course in courses:
		school_courses = courses_by_school.setdefault(course.school_id, [])
		school_courses.append({
			"name": course.name,
			"credit": course.credit,
			"review_count": course.review_count
		})

	return Result.SUCCESS, courses_by_school