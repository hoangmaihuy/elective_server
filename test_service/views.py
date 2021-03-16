from common.utils import parse_request
from test_service.schemas import *
from common.consts import ErrorCode



@parse_request(method="POST", schema=ECHO_SCHEMA)
def echo(request, data):
	return ErrorCode.OK, {
		"message": data["message"]
	}
