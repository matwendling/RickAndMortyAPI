from dataclasses import asdict

from fastapi import APIRouter, status

from app.characters.entrypoint.controllers.find_characters_controller import FindCharactersController
from app.characters.entrypoint.controllers.populate_all_characters_controller import PopulateAllCharactersController
from app.characters.entrypoint.requests.find_character_request import FindCharacterRequest

character_route = APIRouter(prefix="/character")

@character_route.post("/populate") # POST (127.0.0.1:8001/character)
def populate_all() -> int:
    PopulateAllCharactersController().run()
    return status.HTTP_201_CREATED

@character_route.post("/find") # GET (127.0.0.1:8001/character/all)
def get_characters(where: FindCharacterRequest = FindCharacterRequest()) -> list[dict]:
    return FindCharactersController().run(where)