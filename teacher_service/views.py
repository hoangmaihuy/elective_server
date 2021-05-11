from common.utils import parse_request
from common.consts import *


@parse_request(method="GET", login_required=True)
def get_teacher_list(request, data):
	teachers = teacher_manager.get_teacher_names()
	return Result.SUCCESS, teachers