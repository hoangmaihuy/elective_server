ID_SCHEMA = {
    "type": "integer",
    "minimum": 1,
}

SCORE_SCHEMA = {
    "type": "number",
    "minimum": 1,
    "maximum": 5,
}

ADD_REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "content": {
            "type": "string"
        },
        "course_id": ID_SCHEMA,
        "teacher_id": ID_SCHEMA,
        "semester": {
            "type": "string",
            "minLength": 7,
            "maxLength": 7,
        },
        "recommend_score": SCORE_SCHEMA,
        "work_score": SCORE_SCHEMA,
        "exam_score": SCORE_SCHEMA,
        "content_score": SCORE_SCHEMA,
        "user_grade": {
            "type": "number",
            "minimum": 1,
            "maximum": 100,
        }
    },
    "required": ["course_id", "teacher_id", "semester", "recommend_score", "content_score", "work_score", "exam_score"],
}