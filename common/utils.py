import jsonschema
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from common.consts import ErrorCode
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
	print(obj)
	try:
		return json.dumps(obj, encoding='utf-8', ensure_ascii=False)
	except Exception:
		return None


def parse_request(method, schema=None):
	def outer(func):
		@wraps(func)
		def inner(request, *args, **kwargs):
			if request.method != method:
				return HttpResponseBadRequest()
			data = request.body
			if request.content_type == 'application/json':
				data = to_json(data)
				if data is None:
					return HttpResponseBadRequest()
				if schema:
					try:
						jsonschema.validate(data, schema)
					except jsonschema.ValidationError:
						return HttpResponseBadRequest()

			err, reply = func(request, data, *args, **kwargs)

			return HttpResponse(from_json({
				"error": err,
				"reply": reply,
			}))

		return inner

	return outer


# return error, reply
def request_api(url, method="POST", headers=None, data=None):
	if method == "GET":
		r = requests.get(url, headers=headers, params=data)
	elif method == "POST":
		r = requests.post(url, headers=headers, json=data)
	else:
		return ErrorCode.ERR_NOT_SUPPORTED, None

	if r.status_code != 200:
		return r.status_code, None
	resp_data = r.json()
	return resp_data["error"], resp_data["reply"]
