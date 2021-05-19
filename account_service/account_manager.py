from django.utils.crypto import get_random_string
from common.cache import cache_func
from common.utils import TimeUtils
from common.crypto import encode_jwt
from account_service.consts import *
from account_service.models import User
from test_common.consts import TEST_EMAIL, TEST_VERIFICATION_CODE


@cache_func(prefix=VERIFICATION_CODE_CACHE_PREFIX, timeout=VERIFICATION_CODE_CACHE_TIMEOUT)
def generate_verification_code(email):
    if email == TEST_EMAIL:
        auth_code = TEST_VERIFICATION_CODE
    else:
        auth_code = get_random_string(length=6, allowed_chars='0123456789')
    return auth_code


@cache_func(prefix=VERIFICATION_CODE_CACHE_PREFIX, timeout=0)
def get_verification_code_by_email(email):
    return None


def generate_token(user):
    token = encode_jwt({
        "user_id": user.id,
        "email": user.email,
        "last_login": user.last_login,
        "expiry": TimeUtils.now_ts() + TimeUtils.DAY * 7
    })
    return token


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


@cache_func(prefix=GET_USER_BY_ID_CACHE_PREFIX, timeout=GET_USER_BY_ID_CACHE_TIMEOUT)
def get_user_by_id(user_id):
    return User.objects.get(id=user_id)