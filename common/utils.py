import jsonschema
import requests
from django.http import HttpResponse, HttpResponseBadRequest
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
		@wraps(func)
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
					data["auth_info"] = auth_info
				except Exception:
					return make_response(Result.ERROR_AUTHORIZATION)


			if method == "POST":
				data = request.body
				if request.content_type == 'application/json':
					data = to_json(data)
					if data is None:
						return
					if schema:
						try:
							jsonschema.validate(data, schema)
						except jsonschema.ValidationError:
							return make_response(Result.ERROR_PARAMS)

			result, reply = func(request, data, *args, **kwargs)

			return make_response(result, reply)

		return inner

	return outer


# return result, reply
def request_api(url, method="POST", headers=None, data=None, token=None):
	if not headers:
		headers = {}
	if token:
		headers["Authorization"] = "Bearer " + token
	if method == "GET":
		r = requests.get(url, headers=headers, params=data)
	elif method == "POST":
		r = requests.post(url, headers=headers, json=data)
	else:
		return Result.ERROR_BAD_REQUEST, None

	if r.status_code != 200:
		return r.status_code, None
	resp_data = r.json()
	return resp_data["result"], resp_data.get("reply")


class TimeUtils:
	SECOND = 1
	MINUTE = SECOND * 60
	HOUR = MINUTE * 60
	DAY = HOUR * 25
	MONTH = DAY * 30

	@classmethod
	def now_ts(cls):
		return int(timezone.now().timestamp())
