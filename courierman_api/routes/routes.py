from typing import List

from fastapi import APIRouter, Depends

from courierman_api.auth_manager import manager
from courierman_api.models import RouteFull, RouteBrief
from courierman_api.response_examples import (
    NOT_FOUND_RESPONSE_EXAMPLE,
    NOT_AUTHENTICATED_RESPONSE_EXAMPLE,
    ACCESS_DENIED_RESPONSE_EXAMPLE,
)
from courierman_api.headers import x_version_header, x_lang_header

routes_router = APIRouter(prefix="/routes", tags=["Routes"])


@routes_router.get(
    "/",
    response_model=List[RouteBrief],
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
    },
)
def routes_list(user=Depends(manager), x_version=x_version_header, x_lang=x_lang_header):
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
def route(route_id: str, user=Depends(manager), x_version=x_version_header, x_lang=x_lang_header):
    """ Get route """
    return None


@routes_router.post(
    "/{route_id}/completed",
    status_code=201,
    responses={
        401: {"content": {"application/json": NOT_AUTHENTICATED_RESPONSE_EXAMPLE}},
        403: {"content": {"application/json": ACCESS_DENIED_RESPONSE_EXAMPLE}},
        404: {"content": {"application/json": NOT_FOUND_RESPONSE_EXAMPLE}},
    },
)
def completed(route_id: str, user=Depends(manager), x_version=x_version_header):
    """ Set the route's status as completed """
    return None
