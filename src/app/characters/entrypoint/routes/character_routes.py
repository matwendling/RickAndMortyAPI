from dataclasses import asdict

from fastapi import APIRouter, status

from app.characters.domain.dtos.create_character import CreateCharacterDTO
from app.characters.entrypoint.controllers.populate_all_characters_controller import PopulateAllCharactersController
from app.characters.entrypoint.requests.create_character_request import CreateCharacterRequest
from app.characters.entrypoint.requests.find_character_request import FindCharacterRequest
from app.characters.entrypoint.requests.update_character_request import UpdateCharacterRequest
from app.characters.infra.repositories.psycopg_character_repository import PsycopgCharacterRepository

character_route = APIRouter(prefix="/character")

@character_route.post("") # POST (127.0.0.1:8001/character)
def populate_all() -> int:
    PopulateAllCharactersController().run()
    return status.HTTP_201_CREATED

@character_route.get("/all") # GET (127.0.0.1:8001/character/all)
def get_all_characters() -> str:
    return "bananinha"