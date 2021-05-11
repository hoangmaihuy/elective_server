from course_service.models import *


def get_courses_by_params(params, order_by=None, offset=0, limit=1):
	courses = Course.objects.filter(**params)
	if order_by is not None:
		courses = courses.order_by(order_by)
	total = courses.count()
	courses = courses[offset:offset+limit]
	return total, list(courses.values())


def get_courses_by_school_ids(school_ids):
	return Course.objects.filter(school_id__in=school_ids)