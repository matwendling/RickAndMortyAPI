from fastapi import APIRouter

from app.origins.entrypoint.controllers.find_origins_controller import FindOriginsController
from app.origins.entrypoint.requests.find_origin_request import FindOriginsRequest

origin_route = APIRouter(prefix="/origin")

@origin_route.post("/find")
def get_origins(where: FindOriginsRequest = FindOriginsRequest()) -> list[dict]:
    return FindOriginsController().run(where)   