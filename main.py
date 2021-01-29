import uvicorn
from fastapi import FastAPI, APIRouter

from courierman_api.routes import orders_router, routes_router, user_router
from courierman_api.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION

api_router = APIRouter()
api_router.include_router(orders_router)
api_router.include_router(routes_router)
api_router.include_router(user_router)


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(api_router, prefix=API_PREFIX)
    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=False, debug=False)
