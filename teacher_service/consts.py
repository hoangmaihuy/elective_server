from tuike_api.settings import HOST


TEACHER_SERVICE_API = HOST + "/teacher"


class TeacherServiceApi:
	GET_TEACHER_LIST = TEACHER_SERVICE_API + "/get_teacher_list"


GET_TEACHER_NAMES_CACHE_PREFIX = "GET_TEACHER_NAMES"
GET_TEACHER_NAMES_CACHE_TIMEOUT = 60 * 30