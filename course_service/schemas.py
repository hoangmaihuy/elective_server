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
	},
	"required": ["current_page", "page_size"]
}