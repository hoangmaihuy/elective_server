from common.schemas import *

ADD_REVIEW_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "title": STRING_SCHEMA,
        "content": STRING_SCHEMA,
        "course_id": ID_SCHEMA,
        "teacher_id": ID_SCHEMA,
        "semester": SEMESTER_SCHEMA,
        "recommend_score": SCORE_SCHEMA,
        "work_score": SCORE_SCHEMA,
        "exam_score": SCORE_SCHEMA,
        "content_score": SCORE_SCHEMA,
    },
    "required": ["course_id", "teacher_id", "semester", "recommend_score", "content_score", "work_score", "exam_score"],
}

GET_LATEST_REVIEWS_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "offset": {
            "type": "integer",
            "minimum": 0,
        },
        "size": {
            "type": "integer",
            "minimum": 1,
            "maximum": 50,
        },
    },
    "required": ["offset", "size"]
}

REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "id": ID_SCHEMA,
        "title": STRING_SCHEMA,
        "content": STRING_SCHEMA,
        "course_id": ID_SCHEMA,
        "class_id": ID_SCHEMA,
        "teacher_id": ID_SCHEMA,
        "recommend_score": SCORE_SCHEMA,
        "work_score": SCORE_SCHEMA,
        "content_score": SCORE_SCHEMA,
        "exam_score": SCORE_SCHEMA,
        "create_time": UINT_SCHEMA,
        "teacher_name": STRING_SCHEMA,
        "course_name": STRING_SCHEMA,
        "semester": SEMESTER_SCHEMA,
        "likes": UINT_SCHEMA,
        "dislikes": UINT_SCHEMA,
        "interaction": INTERACTION_SCHEMA,
    },
    "required": [
        "id", "title", "content", "course_id", "class_id", "teacher_id",
        "recommend_score", "work_score", "content_score", "exam_score",
        "create_time", "teacher_name", "course_name", "semester", "likes",
        "dislikes", "interaction",
    ]
}

GET_LATEST_REVIEWS_REPLY_SCHEMA = {
    "type": "object",
    "properties": {
        "total": UINT_SCHEMA,
        "reviews": {
            "type": "array",
            "items": REVIEW_SCHEMA,
        }
    },
    "required": ["reviews"]
}

GET_COURSE_REVIEWS_REQUEST_SCHEMA = {
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
        "course_id": ID_SCHEMA,
        "teacher_id": ID_SCHEMA,
        "semester": SEMESTER_SCHEMA,
        "sort_by": {
            "type": "string",
        }
    },
    "required": ["current_page", "page_size", "course_id"]
}

GET_COURSE_REVIEWS_REPLY_SCHEMA = {
    "type": "object",
    "properties": {
        "total": UINT_SCHEMA,
        "reviews": {
            "type": "array",
            "items": REVIEW_SCHEMA,
        }
    },
    "required": ["reviews"]
}

INTERACT_REVIEW_REQUEST_SCHEMA = {
    "type": "object",
    "properties": {
        "review_id": ID_SCHEMA,
        "action": {
            "type": "integer",
            "minimum": -1,
            "maximum": 1,
        },
    },
    "required": ["review_id", "action"],
}
GET_TEACHER_REVIEWS_REQUEST_SCHEMA = {
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
        "teacher_id": ID_SCHEMA,
    },
    "required": ["current_page", "page_size", "teacher_id"],
}

GET_TEACHER_REVIEWS_REPLY_SCHEMA = {
    "type": "object",
    "properties": {
        "total": UINT_SCHEMA,
        "reviews": {
            "type": "array",
            "items": REVIEW_SCHEMA,
        }
    },
    "required": ["total", "reviews"]
}
