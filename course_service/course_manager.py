from common.utils import TimeUtils
from common.cache import cache_func
from common.logger import log
from course_service.models import *
from course_service.consts import *


def get_courses_by_params(params, order_by=None, offset=0, limit=1):
	courses = Course.objects.filter(**params)
	if order_by is not None:
		courses = courses.order_by(order_by)
	total = courses.count()
	courses = courses[offset:offset+limit]
	return total, list(courses.values())


@cache_func(prefix=GET_COURSES_BY_SCHOOL_CACHE_PREFIX, timeout=GET_COURSES_BY_SCHOOL_CACHE_TIMEOUT)
def get_courses_by_school():
	courses = list(Course.objects.all().values("id", "name", "school_id", "course_no", "credit", "review_count"))
	courses_by_school = {}
	for course in courses:
		school_courses = courses_by_school.setdefault(course["school_id"], [])
		school_courses.append(course)
	return courses_by_school


@cache_func(prefix=GET_COURSE_RANK_CACHE_PREFIX, timeout=GET_COURSE_RANK_CACHE_TIMEOUT)
def get_course_rank(course_type, school_id, rank_size):
	qs = Course.objects.filter(type__range=(course_type, course_type+99))
	if school_id:
		qs = qs.filter(school_id=school_id)
	qs = qs.order_by("-recommend_score", "-review_count", "-last_review")
	qs = qs[:rank_size]
	courses = list(qs.values("id", "name", "recommend_score"))
	return courses


@cache_func(prefix=GET_TEACHER_IDS_BY_COURSE_ID_CACHE_PREFIX, timeout=GET_TEACHER_IDS_BY_COURSE_ID_CACHE_TIMEOUT)
def get_teacher_ids_by_course_id(course_id):
	return list(Class.objects.filter(course_id=course_id).values_list("teacher_id", flat=True))


def get_course_infos_by_ids(course_ids):
	courses = Course.objects.filter(id__in=course_ids).values(
		"id", "name", "course_no", "credit", "school_id", "type", "review_count"
	)
	return courses


def update_course_score(course_id, score):
	course = Course.objects.filter(id=course_id).first()
	if not course:
		log.error("update_course_score_course_not_found|course_id=", course_id)
		return False
	review_count = course.review_count
	rate = review_count / (review_count + 1)
	course.recommend_score = course.recommend_score * rate + score["recommend_score"] / (review_count + 1)
	course.content_score = course.content_score * rate + score["content_score"] / (review_count + 1)
	course.work_score = course.work_score * rate + score["work_score"] / (review_count + 1)
	course.exam_score = course.exam_score * rate + score["exam_score"] / (review_count + 1)
	course.review_count = review_count + 1
	course.last_review = TimeUtils.now_ts()
	try:
		course.save()
		return True
	except Exception as e:
		log.error("update_course_score_exception|course_id={},exception={}".format(course_id, e))
		return False
