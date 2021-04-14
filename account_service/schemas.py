REQUEST_AUTH_CODE_SCHEMA = {
	"type": "object",
	"properties": {
		"email": {
			"type": "string"
		}
	},
	"required": ["email"]
}

LOGIN_SCHEMA = {
	"type": "object",
	"properties": {
		"email": {
			"type": "string"
		},
		"auth_code": {
			"type": "string",
			"pattern": "[0-9]{6,6}"
		}
	},
	"required": ["email", "auth_code"]
}
