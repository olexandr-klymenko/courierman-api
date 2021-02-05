from typing import List

from fastapi import APIRouter, Depends

from courierman_api.auth_manager import manager
from courierman_api.models import (
    OrderFull, OrderBrief
)
from courierman_api.response_examples import (
    NOT_FOUND_RESPONSE_EXAMPLE,
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
    ACCESS_DENIED_RESPONSE_EXAMPLE,
)

orders_router = APIRouter(prefix="/orders", tags=["Orders"])


@orders_router.get(
    "/",
    response_model=List[OrderBrief],
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def orders_list(route_id: str, user=Depends(manager)):
    """ Get orders list """
    return []


@orders_router.get(
    "/{order_id}",
    response_model=OrderFull,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def order(order_id: str, user=Depends(manager)):
    """ Get order """
    return None


@orders_router.post(
    "/{order_id}/delivered",
    status_code=201,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def delivered(order_id: str, user=Depends(manager)):
    """ Change order status to delivered """
    return None
