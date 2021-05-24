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

GET_TEACHER_INFO_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"teacher_id": ID_SCHEMA,
	},
	"required": ["teacher_id"]
}

GET_TEACHER_INFO_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"id": ID_SCHEMA,
		"name": TEACHER_NAME_SCHEMA,
		"review_count": UINT_SCHEMA,
		"recommend_score": SCORE_SCHEMA,
		"content_score": SCORE_SCHEMA,
		"work_score": SCORE_SCHEMA,
		"exam_score": SCORE_SCHEMA,
	},
	"required": ["id", "name", "review_count", "recommend_score", "content_score", "work_score", "exam_score"]
}