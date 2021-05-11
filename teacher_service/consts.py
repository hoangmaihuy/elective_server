from tuike_api.settings import HOST


TEACHER_SERVICE_API = HOST + "/teacher"


class TeacherServiceApi:
	GET_TEACHER_LIST = TEACHER_SERVICE_API + "/get_teacher_list"
