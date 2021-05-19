ID_SCHEMA = {
	"type": "integer",
	"minimum": 1,
}

SCORE_SCHEMA = {
	"type": "number",
	"minimum": 0,
	"maximum": 5,
}

SEMESTER_SCHEMA = {
	"type": "string",
	"minLength": 7,
	"maxLength": 7,
}

COURSE_NAME_SCHEMA = {
	"type": "string",
	"maxLength": 50,
}

COURSE_NO_SCHEMA = {
	"type": "string",
	"maxLength": 50,
}

CREDIT_SCHEMA = {
	"type": "integer",
	"minimum": 0,
	"maximum": 20,
}

SCHOOL_ID_SCHEMA = {
	"type": "integer",
	"minimum": 1,
	"maximum": 50,
}

COURSE_TYPE_SCHEMA = {
	"type": "integer",
	"minimum": 100,
	"maximum": 700,
}

RESULT_SCHEMA = {
	"type": "string",
}

STRING_SCHEMA = {
	"type": "string",
	"minLength": 1,
}

UINT_SCHEMA = {
	"type": "integer",
	"minimum": 0,
}

INTERACTION_SCHEMA = {
	"type": "integer",
	"minimum": -1,
	"maximum": 1,
}

TEACHER_NAME_SCHEMA = {
	"type": "string",
	"minLength": 1,
	"maxLength": 50,
}