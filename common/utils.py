import jsonschema
from django.http import HttpResponse, HttpResponseBadRequest
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
