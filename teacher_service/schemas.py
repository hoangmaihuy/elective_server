from common.schemas import *

GET_TEACHERS_BY_COURSE_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"course_id": ID_SCHEMA
	},
	"required": ["course_id"]
}

TEACHER_BASIC_SCHEMA = {
	"type": "object",
	"properties": {
		"id": ID_SCHEMA,
		"name": TEACHER_NAME_SCHEMA,
	},
	"required": ["id", "name"]
}

GET_TEACHERS_BY_COURSE_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"teachers": {
			"type": "array",
			"items": TEACHER_BASIC_SCHEMA,
		}
	},
	"required": ["teachers"]
}