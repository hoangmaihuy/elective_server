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


def get_class(course_id, teacher_id, semester):
	return Class.objects.filter(
		course_id=course_id,
		teacher_id=teacher_id,
		semester=semester,
	).first()


@cache_func(prefix=GET_TEACHER_IDS_BY_COURSE_ID_CACHE_PREFIX, timeout=GET_TEACHER_IDS_BY_COURSE_ID_CACHE_TIMEOUT)
def get_teacher_ids_by_course_id(course_id):
	return list(Class.objects.filter(course_id=course_id).values_list("teacher_id", flat=True))


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

def update_class_score(class_id, score):
	c = Class.objects.filter(id=class_id).first()
	if not c:
		log.error("update_class_score_class_not_found|class_id=", class_id)
		return False
	review_count = c.review_count
	rate = review_count / (review_count + 1)
	c.recommend_score = c.recommend_score * rate + score["recommend_score"] / (review_count + 1)
	c.content_score = c.content_score * rate + score["content_score"] / (review_count + 1)
	c.work_score = c.work_score * rate + score["work_score"] / (review_count + 1)
	c.exam_score = c.exam_score * rate + score["exam_score"] / (review_count + 1)
	c.review_count = review_count + 1
	try:
		c.save()
		return True
	except Exception as e:
		log.error("update_class_score_exception|class_id={},exception={}".format(class_id, e))
		return False