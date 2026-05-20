from dataclasses import asdict

from fastapi import APIRouter, status
from app.classification_types.entrypoint.controllers.find_classification_types_controller import FindClassificationTypesController
from app.classification_types.entrypoint.requests.find_classification_types_request import FindClassificationTypesRequest

classification_types_route = APIRouter(prefix="/classification_types")

@classification_types_route.post("/find")
def get_classification_types(where: FindClassificationTypesRequest = FindClassificationTypesRequest()) -> list[dict]:
    return FindClassificationTypesController().run(where)