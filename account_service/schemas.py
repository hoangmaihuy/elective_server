REQUEST_VERIFICATION_CODE_SCHEMA = {
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
		"verification_code": {
			"type": "string",
			"pattern": "[0-9]{6}"
		}
	},
	"required": ["email", "verification_code"]
}
