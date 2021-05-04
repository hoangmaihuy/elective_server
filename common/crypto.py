import jwt
from tuike_api.settings import SECRET_KEY


def encode_jwt(payload):
	jwt_string = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
	return jwt_string


def decode_jwt(jwt_string):
	try:
		return jwt.decode(jwt_string, SECRET_KEY, algorithms=["HS256"])
	except jwt.InvalidTokenError as e:
		return None
