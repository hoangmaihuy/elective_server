from common.cache import cache_func
from common.logger import log
from course_service import course_manager
from teacher_service.models import *
from teacher_service.consts import *


@cache_func(prefix=GET_TEACHER_NAMES_CACHE_PREFIX, timeout=GET_TEACHER_NAMES_CACHE_TIMEOUT)
def get_teacher_names():
	return list(Teacher.objects.all().values("id", "name"))


@cache_func(prefix=GET_TEACHERS_BY_COURSE_CACHE_PREFIX, timeout=GET_TEACHERS_BY_COURSE_CACHE_TIMEOUT)
def get_teachers_by_course(course_id):
	teacher_ids = course_manager.get_teacher_ids_by_course_id(course_id)
	teachers = list(Teacher.objects.filter(id__in=teacher_ids).values("id", "name"))
	return teachers


def get_teacher_infos_by_ids(teacher_ids):
	return list(Teacher.objects.filter(id__in=teacher_ids).values("id", "name"))


def update_teacher_score(teacher_id, score):
	t = Teacher.objects.filter(id=teacher_id).first()
	if not t:
		log.error("update_teacher_score_teacher_not_found|teacher_id", teacher_id)
		return False
	review_count = t.review_count
	rate = review_count / (review_count + 1)
	t.recommend_score = t.recommend_score * rate + score["recommend_score"] / (review_count + 1)
	t.content_score = t.content_score * rate + score["content_score"] / (review_count + 1)
	t.work_score = t.work_score * rate + score["work_score"] / (review_count + 1)
	t.exam_score = t.exam_score * rate + score["exam_score"] / (review_count + 1)
	t.review_count = review_count + 1
	try:
		t.save()
		return True
	except Exception as e:
		log.error("update_teacher_score_exception|teacher_id={},exception={}".format(teacher_id, e))
		return False