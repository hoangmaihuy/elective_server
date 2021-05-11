from django.db import models


class Teacher(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)
	review_count = models.PositiveIntegerField()
	recommend_score = models.FloatField(default=0)
	exam_score = models.FloatField(default=0)
	work_score = models.FloatField(default=0)
	content_score = models.FloatField(default=0)
	create_time = models.PositiveBigIntegerField()

	class Meta:
		db_table = 'teacher_tab'
		indexes = [
			models.Index(fields=['name'], name='teacher_name_idx')
		]
