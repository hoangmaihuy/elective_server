GET_TEACHERS_BY_COURSE_SCHEMA = {
	"type": "object",
	"properties": {
		"course_id": {
			"type": "integer",
			"minimum": 1,
		}
	},
	"required": ["course_id"]
}