from fastapi import APIRouter

from app.locations.entrypoint.controllers.find_locations_controller import FindLocationsController
from app.locations.entrypoint.requests.find_locations_request import FindLocationsRequest

location_route = APIRouter(prefix="/location")

@location_route.post("/find")
def get_locations(where: FindLocationsRequest = FindLocationsRequest()) -> list[dict]:
    return FindLocationsController().run(where)