from dataclasses import asdict
from app.episodes.domain.repositories import IEpisodeRepository
from app.episodes.domain.dtos import (
    CreateEpisodeDTO, 
    UpdateEpisodeDTO,
    FindEpisodeDTO,
    EpisodeDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgEpisodeRepository(IEpisodeRepository):
    def __init__(self):
        self.manager = PsycopgRepository("episodes", ("id", "url", "num", "season"))

    def create(self, create: CreateEpisodeDTO) -> EpisodeDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return EpisodeDTO(**data)
    
    def create_many(self, create: list[CreateEpisodeDTO]) -> list[EpisodeDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [EpisodeDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindEpisodeDTO = FindEpisodeDTO()) -> list[EpisodeDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [EpisodeDTO(**episode) for episode in response]
    
    def update(self, uuid: str, update: UpdateEpisodeDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)