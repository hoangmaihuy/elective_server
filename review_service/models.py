from django.db import models


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    course_id = models.PositiveBigIntegerField()
    class_id = models.PositiveBigIntegerField()
    teacher_id = models.PositiveBigIntegerField()
    recommend_score = models.FloatField(default=0)
    exam_score = models.FloatField(default=0)
    work_score = models.FloatField(default=0)
    content_score = models.FloatField(default=0)
    create_by = models.PositiveBigIntegerField()
    create_time = models.PositiveBigIntegerField()

    class Meta:
        db_table = 'review_tab'
        indexes = [
            models.Index(fields=['course_id'], name='review_course_id_idx'),
            models.Index(fields=['class_id'], name='review_class_id_idx'),
            models.Index(fields=['teacher_id'], name='review_teacher_id_idx'),
            models.Index(fields=['create_time'], name='review_create_time'),
        ]
