import jsonschema
import requests
from django.http import HttpResponse, HttpResponseBadRequest
from common.consts import Result
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

def make_response(result, reply=None):
	data = {
		"result": result
	}
	if reply is not None:
		data["reply"] = reply
	return HttpResponse(from_json(data))

def parse_request(method, schema=None):
	def outer(func):
		@wraps(func)
		def inner(request, *args, **kwargs):
			if request.method != method:
				return make_response(Result.ERROR_BAD_REQUEST)

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
def request_api(url, method="POST", headers=None, data=None):
	if method == "GET":
		r = requests.get(url, headers=headers, params=data)
	elif method == "POST":
		r = requests.post(url, headers=headers, json=data)
	else:
		return Result.ERROR_BAD_REQUEST, None

	if r.status_code != 200:
		return r.status_code, None
	resp_data = r.json()
	return resp_data["result"], resp_data["reply"]
