from teacher_service.models import *


def get_teacher_names():
	return Teacher.objects.all().values(["id", "name"])

