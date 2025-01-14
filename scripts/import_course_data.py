import django
import os
import sys
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuike_api.settings")
django.setup()

from course_service.consts import CourseTypeEnum, SchoolEnum
from course_service.models import Course, Class
from teacher_service.models import Teacher
from common.utils import TimeUtils
import simplejson as json

BATCH_SIZE = 500
COURSE_DATA_DIR = 'courses_data'
COURSE_TYPE_MAP = {
	"speciality": "专业课",
	"english": "英语课",
	"politics": "政治课",
	"gym": "体育课",
	"liberal_computer": "计算机基础课",
	"pub_choice": "公选课",
	"trans_choice": "通选课",
}



def import_courses(course_type):
	filename = os.path.join(os.getcwd(), COURSE_DATA_DIR, course_type + '.json')
	with open(filename, "r", encoding='utf8') as f:
		courses = json.load(f)
	course_objs = []
	teacher_names = []
	for course in courses:
		school_id = SchoolEnum.get(course['school'])
		if school_id is None:
			print("No school_id for {}".format(course['school']))
			continue
		type_name = COURSE_TYPE_MAP[course_type]
		if course_type == 'english':
			type_name = type_name + course['level']
		elif course_type == 'trans_choice':
			type_name = type_name + course['type']
		type_id = CourseTypeEnum.get(type_name)
		if type_id is None:
			print("No type_id for {}".format(type_name))
			continue
		credit = course['credits'] if course_type in ['english', 'trans_choice'] else course['credit']
		teacher_names.extend(course['teachers'])
		course_obj = Course(
			name=course['name'],
			course_no=course['id'],
			credit=credit,
			school_id=school_id,
			type=type_id,
			review_count=0,
			last_review=0,
			create_time=TimeUtils.now_ts(),
		)
		course_objs.append(course_obj)
	print("bulk_create courses {}".format(course_type))
	Course.objects.bulk_create(course_objs)
	print("bulk_create courses finished")

	teacher_names = list(set(teacher_names))
	created_names = set(Teacher.objects.filter(name__in=teacher_names).values_list("name", flat=True))
	teacher_objs = [
		Teacher(
			name=name,
			review_count=0,
			create_time=TimeUtils.now_ts()
		)
		for name in teacher_names if name not in created_names
	]
	print("bulk_create teachers")
	Teacher.objects.bulk_create(teacher_objs)
	print("bulk_create teachers finished")

	class_objs = []

	for course in courses:
		school_id = SchoolEnum.get(course['school'])
		course_id = Course.objects.filter(name=course['name'], school_id=school_id).first().id
		teachers = list(Teacher.objects.filter(name__in=course['teachers']))
		for teacher in teachers:
			class_objs.append(Class(
				course_id=course_id,
				teacher_id=teacher.id,
				semester="20-21-2",
				review_count=0,
				create_time=TimeUtils.now_ts()
			))
	print("bulk_create classes")
	Class.objects.bulk_create(class_objs)
	print("bulk_create classes finished")

if __name__ == '__main__':
	import_courses('speciality')
	import_courses('gym')
	import_courses('english')
	import_courses('liberal_computer')
	import_courses('politics')
	import_courses('pub_choice')
	import_courses('trans_choice')