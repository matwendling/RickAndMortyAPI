from fastapi import APIRouter

from app.species.entrypoint.controllers.find_species_controller import FindSpeciesController
from app.species.entrypoint.requests.find_specie_request import FindSpecieRequest

specie_route = APIRouter(prefix="/specie")

@specie_route.post("/find")
def get_species(where: FindSpecieRequest = FindSpecieRequest()) -> list[dict]:
    return FindSpeciesController().run(where)