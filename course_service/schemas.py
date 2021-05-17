GET_COURSE_LIST_SCHEMA = {
	"type": "object",
	"properties": {
		"current_page": {
			"type": "integer",
			"minimum": 1,
		},
		"page_size": {
			"type": "integer",
			"minimum": 1,
			"maximum": 100,
		},
		"course_no": {
			"type": "string",
			"max_length": 20,
		},
		"name": {
			"type": "string",
			"max_length": 50,
		},
		"type": {
			"type": "integer",
		},
		"school_id": {
			"type": "integer",
		},
		"order_by": {
			"type": "string",
		}
	},
	"required": ["current_page", "page_size"]
}


GET_COURSE_RANK_SCHEMA = {
	"type": "object",
	"properties": {
		"course_type": {
			"type": "integer",
			"minimum": 1,
		},
		"school_id": {
			"type": "integer",
			"minimum": 1,
		},
		"rank_size": {
			"type": "integer",
			"minimum": 1,
			"maximum": 50,
		},
	},
	"required": ["course_type"]
}