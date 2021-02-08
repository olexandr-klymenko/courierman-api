NOT_FOUND_RESPONSE_EXAMPLE = {
    "example": {
        "detail": [
            {"loc": ["body", "__root__"], "msg": "Not found", "type": "not_found"}
        ]
    }
}

NOT_AUTHENTICATED_RESPONSE_EXAMPLE = {
    "example": {
        "detail": [
            {
                "loc": ["body", "__root__"],
                "msg": "Not authenticated",
                "type": "not_authenticated",
            }
        ]
    }
}

ACCESS_DENIED_RESPONSE_EXAMPLE = {
    "example": {
        "detail": [
            {
                "loc": ["body", "__root__"],
                "msg": "Access denied",
                "type": "access_denied",
            }
        ]
    }
}

CANT_ESTABLISH_CALL_RESPONSE_EXAMPLE = {
    "example": {
        "detail": [
            {
                "loc": ["body", "__root__"],
                "msg": "Can't establish call",
                "type": "call_failed",
            }
        ]
    },
}
