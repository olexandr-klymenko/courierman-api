from fastapi import APIRouter, Depends

from courierman_api.auth_manager import manager
from courierman_api.models import PasswordChangeRequest, UserInfo
from courierman_api.response_examples import (
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
    ACCESS_DENIED_RESPONSE_EXAMPLE,
)
from courierman_api.headers import x_version_header, x_lang_header

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.get(
    "/me",
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
    response_model=UserInfo,
)
def info(user=Depends(manager), x_version=x_version_header, x_lang=x_lang_header):
    return None


@user_router.post(
    "/password_change",
    status_code=201,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def password_change(
    password: PasswordChangeRequest,
    user=Depends(manager),
    x_version=x_version_header,
):
    return None
