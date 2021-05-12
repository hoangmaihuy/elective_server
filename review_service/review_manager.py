from django.db import IntegrityError, transaction
from common.utils import TimeUtils
from review_service.models import *
from course_service import course_manager
from teacher_service import teacher_manager


@transaction.atomic()
def create_review(course_id, teacher_id, class_id, title, content, score, create_by):
	try:
		with transaction.atomic():
			review = Review.objects.create(
				course_id=course_id,
				class_id=class_id,
				teacher_id=teacher_id,
				title=title,
				content=content,
				**score,
				create_by=create_by,
				create_time=TimeUtils.now_ts()
			)
			if not review:
				return False
			if not course_manager.update_course_score(course_id, score):
				raise IntegrityError
			if not course_manager.update_class_score(class_id, score):
				raise IntegrityError
			if not teacher_manager.update_teacher_score(teacher_id, score):
				raise IntegrityError
			return True
	except IntegrityError as e:
		print(e)
		return False
