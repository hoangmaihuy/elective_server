from common.utils import parse_request
from account_service.schemas import *
from account_service.consts import *



@parse_request(method="POST")
def echo(request, data):
	return ErrorCode.OK, {
		"message": data["message"]
	}
