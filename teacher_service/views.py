from common.utils import parse_request
from common.consts import *
from teacher_service import teacher_manager
from teacher_service.schemas import *


@parse_request(method="GET", login_required=True)
def get_teacher_list(request, data):
	teachers = teacher_manager.get_teacher_names()
	return Result.SUCCESS, teachers


@parse_request(method="POST", schema=GET_TEACHERS_BY_COURSE_REQUEST_SCHEMA, login_required=True)
def get_teachers_by_course(request, data):
	course_id = data["course_id"]
	teachers = teacher_manager.get_teachers_by_course(course_id)
	return Result.SUCCESS, {
		"teachers": teachers
	}