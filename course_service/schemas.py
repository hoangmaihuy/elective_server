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
			"type": "array",
		}
	},
	"required": ["current_page", "page_size"]
}