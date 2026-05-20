from dataclasses import asdict, fields
from app.species.domain.repositories import ISpecieRepository
from app.species.domain.dtos import (
    CreateSpecieDTO, 
    UpdateSpecieDTO,
    FindSpecieDTO,
    SpecieDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgSpecieRepository(ISpecieRepository):
    def __init__(self):
        dto_keys = [f.name for f in fields(SpecieDTO)]
        self.manager = PsycopgRepository("species", dto_keys)

    def create(self, create: CreateSpecieDTO) -> SpecieDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return SpecieDTO(**data)
    
    def create_many(self, create: list[CreateSpecieDTO]) -> list[SpecieDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [SpecieDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindSpecieDTO = FindSpecieDTO()) -> list[SpecieDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [SpecieDTO(**specie) for specie in response]
    
    def update(self, uuid: str, update: UpdateSpecieDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)