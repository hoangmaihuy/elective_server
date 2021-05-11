from common.utils import parse_request
from common.consts import *
from review_service.schemas import *


@parse_request(method="POST", schema=ADD_REVIEW_SCHEMA, auth_required=True)
def add_review(request, data):
    return Result.SUCCESS, None
