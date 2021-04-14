from apt.progress.text import _
from django.db import models

# Create your models here.

class User(models.Model):
	id = models.BigAutoField(primary_key=True)
	email = models.EmailField(unique=True)
	is_superuser = models.BooleanField()
	is_staff = models.BooleanField()
	last_login = models.PositiveBigIntegerField()
	create_time = models.PositiveBigIntegerField()

	class Meta:
		db_table = 'user_tab'
		indexes = [
			models.Index(fields=['email'], name='email_idx')
		]
