from dataclasses import asdict, fields
from app.locations.domain.repositories import ILocationRepository
from app.locations.domain.dtos import (
    CreateLocationDTO, 
    UpdateLocationDTO,
    FindLocationDTO,
    LocationDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgLocationRepository(ILocationRepository):
    def __init__(self):
        dto_keys = [f.name for f in fields(LocationDTO)]
        self.manager = PsycopgRepository("locations", dto_keys)

    def create(self, create: CreateLocationDTO) -> LocationDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return LocationDTO(**data)
    
    def create_many(self, create: list[CreateLocationDTO]) -> list[LocationDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [LocationDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindLocationDTO = FindLocationDTO()) -> list[LocationDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [LocationDTO(**location) for location in response]
    
    def update(self, uuid: str, update: UpdateLocationDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)