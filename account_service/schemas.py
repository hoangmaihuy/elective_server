from common.schemas import *

REQUEST_VERIFICATION_CODE_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"email": {
			"type": "string"
		}
	},
	"required": ["email"]
}

LOGIN_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"email": {
			"type": "string"
		},
		"verification_code": {
			"type": "string",
			"pattern": "[0-9]{6}"
		}
	},
	"required": ["email", "verification_code"]
}

LOGIN_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"access_token": {
			"type": "string",
		},
	},
	"required": ["access_token"]
}

GET_USER_INFO_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"user_id": ID_SCHEMA,
		"authority": STRING_SCHEMA,
		"email": STRING_SCHEMA,
		"expiry": UINT_SCHEMA,
	},
	"required": ["user_id", "authority", "email", "expiry"]
}
