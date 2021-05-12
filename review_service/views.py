from common.utils import parse_request
from common.validator import is_valid_semester
from common.consts import *
from review_service.schemas import *
from review_service import review_manager
from course_service import course_manager


@parse_request(method="POST", schema=ADD_REVIEW_SCHEMA, login_required=True)
def add_review(request, data):
    course_id = data["course_id"]
    teacher_id = data["teacher_id"]
    semester = data["semester"]
    title = data.get("title", "")
    content = data.get("content", "")
    if not is_valid_semester(semester):
        return Result.ERROR_PARAMS, None

    course_class = course_manager.get_class(course_id, teacher_id, semester)
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

