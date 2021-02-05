from typing import List

from fastapi import APIRouter, Depends

from courierman_api.auth_manager import manager
from courierman_api.models import (
    RouteFull, RouteBrief
)
from courierman_api.response_examples import (
    NOT_FOUND_RESPONSE_EXAMPLE,
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
    ACCESS_DENIED_RESPONSE_EXAMPLE,
)

routes_router = APIRouter(prefix="/routes", tags=["Routes"])


@routes_router.get(
    "/",
    response_model=List[RouteBrief],
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def routes_list(user=Depends(manager)):
    """ Get routes list """
    return []


@routes_router.get(
    "/{route_id}",
    response_model=RouteFull,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def route(route_id: str, user=Depends(manager)):
    """ Get route """
    return None
