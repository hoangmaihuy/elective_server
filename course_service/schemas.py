from common.schemas import *

GET_COURSE_LIST_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"current_page": UINT_SCHEMA,
		"page_size": UINT_SCHEMA,
		"course_no": COURSE_NO_SCHEMA,
		"course_name": COURSE_NAME_SCHEMA,
		"course_type": COURSE_TYPE_SCHEMA,
		"school_id": SCHOOL_ID_SCHEMA,
		"order_by": STRING_SCHEMA,
	},
	"required": ["current_page", "page_size"]
}

COURSE_LIST_ITEM_SCHEMA = {
	"type": "object",
	"properties": {
		"id": ID_SCHEMA,
		"name": COURSE_NAME_SCHEMA,
		"course_no": COURSE_NO_SCHEMA,
		"credit": CREDIT_SCHEMA,
		"school_id": SCHOOL_ID_SCHEMA,
		"type": COURSE_TYPE_SCHEMA,
		"review_count": UINT_SCHEMA,
		"recommend_score": SCORE_SCHEMA,
		"exam_score": SCORE_SCHEMA,
		"work_score": SCORE_SCHEMA,
		"content_score": SCORE_SCHEMA,
		"last_review": UINT_SCHEMA,
		"create_time": UINT_SCHEMA,
	},
	"required": [
		"id", "name", "course_no", "credit", "school_id", "type",
		"review_count", "recommend_score", "exam_score", "work_score",
		"content_score", "last_review"
	]
}

GET_COURSE_LIST_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"total": {
			"type": "integer",
			"minimum": 0,
		},
		"courses": {
			"type": "array",
			"items": COURSE_LIST_ITEM_SCHEMA,
		}
	},
	"required": ["total", "courses"]
}

COURSE_BY_SCHOOL_ITEM_SCHEMA = {
	"type": "object",
	"properties": {
		"id": ID_SCHEMA,
		"name": COURSE_NAME_SCHEMA,
		"school_id": SCHOOL_ID_SCHEMA,
		"course_no": COURSE_NO_SCHEMA,
		"credit": CREDIT_SCHEMA,
		"review_count": UINT_SCHEMA,
	},
	"required": ["id", "name", "school_id", "course_no", "credit", "review_count"]
}

GET_COURSES_BY_SCHOOL_REPLY_SCHEMA = {
	"type": "object",
	"patternProperties": {
		"^\d{1,2}$": {
			"type": "array",
			"items": COURSE_BY_SCHOOL_ITEM_SCHEMA,
		}
	},
}

GET_COURSE_RANK_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"course_type": COURSE_TYPE_SCHEMA,
		"school_id": SCHOOL_ID_SCHEMA,
		"rank_size": {
			"type": "integer",
			"minimum": 1,
			"maximum": 50,
		},
	},
	"required": ["course_type"]
}

COURSE_RANK_ITEM_SCHEMA = {
	"type": "object",
	"properties": {
		"id": ID_SCHEMA,
		"name": COURSE_NAME_SCHEMA,
		"recommend_score": SCORE_SCHEMA,
	},
	"required": ["id", "name", "recommend_score"]
}

GET_COURSE_RANK_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"courses": {
			"type": "array",
			"items": COURSE_RANK_ITEM_SCHEMA,
		}
	},
	"required": ["courses"]
}

GET_COURSE_INFO_REQUEST_SCHEMA = {
	"type": "object",
	"properties": {
		"course_id": ID_SCHEMA,
	},
	"required": ["course_id"],
}

GET_COURSE_INFO_REPLY_SCHEMA = {
	"type": "object",
	"properties": {
		"id": ID_SCHEMA,
		"name": COURSE_NAME_SCHEMA,
		"course_no": COURSE_NO_SCHEMA,
		"credit": CREDIT_SCHEMA,
		"school_id": SCHOOL_ID_SCHEMA,
		"type": COURSE_TYPE_SCHEMA,
		"review_count": UINT_SCHEMA,
		"recommend_score": SCORE_SCHEMA,
		"exam_score": SCORE_SCHEMA,
		"work_score": SCORE_SCHEMA,
		"content_score": SCORE_SCHEMA,
		"last_review": UINT_SCHEMA,
		"create_time": UINT_SCHEMA,
	},
	"required": [
		"id", "name", "course_no", "credit", "school_id", "type",
		"review_count", "recommend_score", "exam_score", "work_score",
		"content_score", "last_review", "create_time",
	]
}