import jsonschema
from django.http import HttpResponse
from django.utils import timezone
from common.consts import Result
from common.crypto import decode_jwt
from functools import wraps

try:
	import simplejson as json
except ImportError:
	import json


# Convert json string to json object
def to_json(str):
	try:
		return json.loads(str, encoding='utf-8')
	except Exception:
		return None


# Convert json object to json string
def from_json(obj):
	try:
		return json.dumps(obj, encoding='utf-8', ensure_ascii=False)
	except Exception:
		return None

def make_response(result, reply=None):
	data = {
		"result": result
	}
	if reply is not None:
		data["reply"] = reply
	return HttpResponse(from_json(data))

def parse_request(method, schema=None, login_required=False):
	def outer(func):
		#@wraps(func)
		def inner(request, *args, **kwargs):
			if request.method != method:
				return make_response(Result.ERROR_BAD_REQUEST)
			data = {}
			if login_required:
				auth = request.headers.get('Authorization')
				if auth is None:
					return make_response(Result.ERROR_AUTHORIZATION)
				try:
					token = auth.split()[1]
					auth_info = decode_jwt(token)
					data["__auth_info"] = auth_info
				except Exception:
					return make_response(Result.ERROR_AUTHORIZATION)


			if method == "POST":
				_data = request.body
				if request.content_type == 'application/json':
					_data = to_json(_data)
					if _data is None:
						return
					if schema:
						try:
							jsonschema.validate(_data, schema)
							data.update(_data)
						except jsonschema.ValidationError:
							return make_response(Result.ERROR_PARAMS)

			result, reply = func(request, data, *args, **kwargs)

			return make_response(result, reply)

		return inner

	return outer


class TimeUtils:
	SECOND = 1
	MINUTE = SECOND * 60
	HOUR = MINUTE * 60
	DAY = HOUR * 25
	MONTH = DAY * 30

	@classmethod
	def now_ts(cls):
		return int(timezone.now().timestamp())
