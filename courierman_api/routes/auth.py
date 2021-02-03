from fastapi import APIRouter

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from courierman_api.auth_manager import load_user, manager

auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/token")
def login(data: OAuth2PasswordRequestForm = Depends()):
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
    return {"access_token": access_token, "token_type": "bearer"}
