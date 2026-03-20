from dataclasses import asdict
from app.origins.domain.repositories import IOriginRepository
from app.origins.domain.dtos import (
    CreateOriginDTO, 
    UpdateOriginDTO,
    FindOriginDTO,
    OriginDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgOriginRepository(IOriginRepository):
    def __init__(self):
        self.manager = PsycopgRepository("origins", ("id", "name"))

    def create(self, create: CreateOriginDTO) -> OriginDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return OriginDTO(**data)
    
    def create_many(self, create: list[CreateOriginDTO]) -> list[OriginDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [OriginDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindOriginDTO = FindOriginDTO()) -> list[OriginDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [OriginDTO(**origin) for origin in response]
    
    def update(self, uuid: str, update: UpdateOriginDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)