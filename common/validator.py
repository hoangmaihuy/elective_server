from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def is_pku_mail(email):
	try:
		validate_email(email)
		return email.endswith("pku.edu.cn")
	except ValidationError as e:
		return False


def is_valid_semester(semester):
	if len(semester) != 7:
		return False
	try:
		s = list(map(int, semester.split("-")))
		if len(s) != 3 or s[0] + 1 != s[1] or s[2] > 3 or s[2] < 1:
			return False
		return True
	except Exception as e:
		print(e)
		return False
