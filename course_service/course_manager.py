from course_service.models import *


def get_courses_by_params(params, order_by, offset=0, limit=1):
	courses = Course.objects.filter(**params)
	if order_by:
		courses.order_by(*order_by)
	total = courses.count()
	courses = courses[offset:offset+limit]
	return total, list(courses.values())
