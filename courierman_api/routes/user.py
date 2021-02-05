from fastapi import APIRouter, Depends

from courierman_api.auth_manager import manager
from courierman_api.models import PasswordChangeRequest, UserInfo
from courierman_api.response_examples import (
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
    ACCESS_DENIED_RESPONSE_EXAMPLE,
)

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get(
    "/me",
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
    response_model=UserInfo,
)
def info(user=Depends(manager)):
    return None


@user_router.post(
    "/password_change",
    status_code=201,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def password_change(password_change: PasswordChangeRequest, user=Depends(manager)):
    return None


@user_router.post("/password_recovery", status_code=201)
def password_recovery(phone_number: str):
    return None
