from common.utils import parse_request
from common.consts import *
from account_service.schemas import *
from account_service.account_manager import *
from tuike_consumer.tasks import send_verification_code


@parse_request(method="POST", schema=REQUEST_VERIFICATION_CODE_SCHEMA)
def request_verification_code(request, data):
	email = data["email"]

	if not is_pku_mail(email):
		return Result.ERROR_INVALID_EMAIL, None

	auth_code = generate_verification_code(email)
	send_verification_code(email, auth_code)
	return Result.SUCCESS, None


@parse_request(method="POST", schema=LOGIN_SCHEMA)
def login(request, data):
	email = data["email"]
	verification_code = data["verification_code"]
	if verification_code != get_verification_code_by_email(email):
		return Result.ERROR_VERIFICATION_CODE, None
	user = get_or_create_user_by_email(email)
	token = generate_token(user)
	return Result.SUCCESS, {
		"access_token": token
	}


@parse_request(method="GET", login_required=True)
def get_user_info(request, data):
	user_id = data["auth_info"]["user_id"]
	user = get_user_by_id(user_id)
	if user is None:
		return Result.ERROR_AUTHORIZATION, None

	authority = "admin" if user.is_superuser else "user"
	return Result.SUCCESS, {
		"user_id": user.id,
		"email": user.email,
		"authority": authority,
		"expiry": data["auth_info"]["expiry"],
	}
