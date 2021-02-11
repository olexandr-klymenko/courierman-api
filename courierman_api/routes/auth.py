from fastapi import APIRouter

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from courierman_api.auth_manager import load_user, manager
from courierman_api.models import LoginResponse
from courierman_api.headers import x_version_header
from courierman_api.response_examples import (
    ACCESS_DENIED_RESPONSE_EXAMPLE,
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
)

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/token", response_model=LoginResponse)
def login(data: OAuth2PasswordRequestForm = Depends()):
    """
    Get access token.
    username: phone number
    """
    phone_number = data.username
    password = data.password

    user = load_user(
        phone_number
    )  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user["password"]:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(data=dict(sub=phone_number))
    return {"access_token": access_token}


@auth_router.post(
    "/logout",
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def logout(user=Depends(manager), x_version=x_version_header):
    return None
