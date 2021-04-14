import jwt
from tuike_api.settings import SECRET_KEY, EMAIL_HOST_USER
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.validators import validate_email, ValidationError
from common.cache import cache_func
from common.utils import TimeUtils
from account_service.consts import *
from account_service.models import User


def is_pku_mail(email):
	try:
		validate_email(email)
		return email.endswith("pku.edu.cn")
	except ValidationError as e:
		return False


@cache_func(prefix=AUTH_CODE_CACHE_PREFIX, timeout=AUTH_CODE_CACHE_TIMEOUT)
def generate_auth_code(email):
	if email == TEST_EMAIL:
		auth_code = TEST_AUTH_CODE
	else:
		auth_code = get_random_string(length=6, allowed_chars='0123456789')
	return auth_code


@cache_func(prefix=AUTH_CODE_CACHE_PREFIX, timeout=0)
def get_auth_code_by_email(email):
	return None


def send_auth_code(to_email, auth_code):
	message = "【推课网】验证码：{}，有效5分钟，请凭验证码登陆。".format(auth_code)
	try:
		send_mail(
			subject="【推课网】登陆验证码",
			message=message,
			from_email=EMAIL_HOST_USER,
			recipient_list=[to_email],
			fail_silently=False
		)
		return True
	except Exception as e:
		print(e)
		return False


def generate_token(user):
	token = jwt.encode({
		"user_id": user.id,
		"email": user.email,
		"last_login": user.last_login,
		"expiry": TimeUtils.now_ts() + TimeUtils.DAY * 7
	}, SECRET_KEY, algorithm="HS256")
	return token


def decode_token(token):
	try:
		return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
	except jwt.InvalidTokenError as e:
		return None


def get_or_create_user_by_email(email):
	defaults = {
		'is_superuser': False,
		'is_staff': False,
		'last_login': TimeUtils.now_ts(),
		'create_time': TimeUtils.now_ts(),
	}
	user, created = User.objects.get_or_create(
		email=email,
		defaults=defaults
	)

	return user

