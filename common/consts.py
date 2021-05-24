from tuike_api.settings import HOST

ACCOUNT_SERVICE_API = HOST + "/account"
COURSE_SERVICE_API = HOST + "/course"
REVIEW_SERVICE_API = HOST + "/review"
TEACHER_SERVICE_API = HOST + "/teacher"


class AccountServiceApi:
	REQUEST_VERIFICATION_CODE = ACCOUNT_SERVICE_API + "/request_verification_code"
	LOGIN = ACCOUNT_SERVICE_API + "/login"
	GET_USER_INFO = ACCOUNT_SERVICE_API + "/get_user_info"


class CourseServiceApi:
	GET_COURSE_LIST = COURSE_SERVICE_API + "/get_course_list"
	GET_COURSES_BY_SCHOOL = COURSE_SERVICE_API + "/get_courses_by_school"
	GET_COURSE_RANK = COURSE_SERVICE_API + "/get_course_rank"
	GET_COURSE_INFO = COURSE_SERVICE_API + "/get_course_info"


class ReviewServiceApi:
	ADD_REVIEW = REVIEW_SERVICE_API + "/add_review"
	GET_LATEST_REVIEWS = REVIEW_SERVICE_API + "/get_latest_reviews"
	GET_COURSE_REVIEWS = REVIEW_SERVICE_API + "/get_course_reviews"
	INTERACT_REVIEW = REVIEW_SERVICE_API + "/interact_review"


class TeacherServiceApi:
	GET_TEACHER_LIST = TEACHER_SERVICE_API + "/get_teacher_list"
	GET_TEACHERS_BY_COURSE = TEACHER_SERVICE_API + "/get_teachers_by_course"
	GET_TEACHER_INFO = TEACHER_SERVICE_API + "/get_teacher_info"


class Result:
	SUCCESS = "success"
	ERROR_BAD_REQUEST = "error_bad_request"
	ERROR_PARAMS = "error_params"
	ERROR_SERVER = "error_server"
	ERROR_INVALID_EMAIL = "error_invalid_email"
	ERROR_VERIFICATION_CODE = "error_verification_code"
	ERROR_AUTHORIZATION = "error_authorization"
	ERROR_CLASS_NOT_EXIST = "error_class_not_exist"
	ERROR_COURSE_NOT_FOUND = "error_course_not_found"
	ERROR_TEACHER_NOT_FOUND = "error_teacher_not_found"
