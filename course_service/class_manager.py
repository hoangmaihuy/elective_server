from common.logger import log
from course_service.models import Class


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


def get_class(course_id, teacher_id, semester):
	return Class.objects.filter(
		course_id=course_id,
		teacher_id=teacher_id,
		semester=semester,
	).first()


def get_class_infos_by_ids(class_ids):
	return list(Class.objects.filter(id__in=class_ids).values(
		"id", "course_id", "teacher_id", "semester", "review_count"
	))
