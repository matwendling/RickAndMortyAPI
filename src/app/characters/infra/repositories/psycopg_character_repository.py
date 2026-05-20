from dataclasses import asdict, fields
from uuid import uuid4

import psycopg2
from app.characters.domain.repositories import ICharacterRepository
from app.characters.domain.dtos import (
    CreateCharacterDTO, 
    UpdateCharacterDTO,
    FindCharacterDTO,
    CharacterDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgCharacterRepository(ICharacterRepository):
    def __init__(self):
        dto_keys = [f.name for f in fields(CharacterDTO)]
        self.manager = PsycopgRepository(
            "characters", dto_keys
        )

    def create(self, create: CreateCharacterDTO) -> CharacterDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return CharacterDTO(**data)
    
    def create_many(self, create: list[CreateCharacterDTO]) -> list[CharacterDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [CharacterDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindCharacterDTO = FindCharacterDTO()) -> list[CharacterDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [CharacterDTO(**character) for character in response]
    
    def update(self, uuid: str, update: UpdateCharacterDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)