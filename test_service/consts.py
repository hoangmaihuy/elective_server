from elective_server.settings import HOST
from enum import Enum

TEST_SERVICE_API = HOST + "/test"


class Api:
	ECHO = TEST_SERVICE_API + "/echo"
