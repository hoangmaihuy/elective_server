import jsonschema


def validate_reply(reply, schema):
	try:
		jsonschema.validate(reply, schema)
		return True
	except jsonschema.ValidationError as e:
		print(e)
		return False
