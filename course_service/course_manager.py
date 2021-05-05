from course_service.models import *


def get_all_courses(offset=0, limit=1, order_by=None):
	courses = Course.objects.all()
	if order_by:
		courses.order_by(order_by)
	total = courses.count()
	courses = courses[offset:offset+limit]
	return total, list(courses.values())
