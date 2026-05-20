from dataclasses import asdict, fields
from app.classification_types.domain.repositories import IClassificationTypeRepository
from app.classification_types.domain.dtos import (
    CreateClassificationTypeDTO, 
    UpdateClassificationTypeDTO,
    FindClassificationTypeDTO,
    ClassificationTypeDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgClassificationTypeRepository(IClassificationTypeRepository):
    def __init__(self):
        dto_keys = [f.name for f in fields(ClassificationTypeDTO)]
        self.manager = PsycopgRepository("classification_types", dto_keys)

    def create(self, create: CreateClassificationTypeDTO) -> ClassificationTypeDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return ClassificationTypeDTO(**data)
    
    def create_many(self, create: list[CreateClassificationTypeDTO]) -> list[ClassificationTypeDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [ClassificationTypeDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindClassificationTypeDTO = FindClassificationTypeDTO()) -> list[ClassificationTypeDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [ClassificationTypeDTO(**classification_type) for classification_type in response]
    
    def update(self, uuid: str, update: UpdateClassificationTypeDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)