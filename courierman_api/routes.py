from typing import List, Optional

from fastapi import APIRouter, Header

from courierman_api.models import (
    Order,
    Route,
    LoginRequest,
    LoginResponse,
    PasswordChangeRequest,
)
from courierman_api.response_examples import (
    NOT_FOUND_RESPONSE_EXAMPLE,
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
    ACCESS_DENIED_RESPONSE_EXAMPLE,
)

orders_router = APIRouter(prefix="/orders", tags=["Orders"])


@orders_router.get(
    "/",
    response_model=List[Order],
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def orders_list(route_id: str, token: Optional[str] = Header(None)):
    """ Get orders list """
    return []


@orders_router.get(
    "/{order_id}",
    response_model=Order,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def order(order_id: str, token: Optional[str] = Header(None)):
    """ Get order """
    return None


@orders_router.post(
    "/{order_id}",
    status_code=201,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def deliver_order(order_id: str, token: Optional[str] = Header(None)):
    """ Change order status to delivered """
    return None


routes_router = APIRouter(prefix="/routes", tags=["Routes"])


@routes_router.get(
    "/",
    response_model=List[Route],
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def routes_list(courier_id: str, token: Optional[str] = Header(None)):
    """ Get routes list """
    return []


@routes_router.get(
    "/{route_id}",
    response_model=Route,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def route(route_id: str, token: Optional[str] = Header(None)):
    """ Get route """
    return None


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post(
    "/login",
    status_code=201,
    response_model=LoginResponse,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def login(login: LoginRequest):
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
    password_change: PasswordChangeRequest, token: Optional[str] = Header(None)
):
    return None


@user_router.post("/password_recovery", status_code=201)
def password_recovery(phone_number: str):
    return None
