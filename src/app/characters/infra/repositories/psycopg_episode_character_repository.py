from dataclasses import asdict
from app.characters.domain.repositories.i_episode_character_repository import IEpisodeCharacterRepository
from app.characters.domain.dtos.episodes import (
    CreateEpisodeCharacterDTO,
    UpdateEpisodeCharacterDTO,
    FindEpisodeCharacterDTO,
    EpisodeCharacterDTO
)
from framework.database.psycopg_repository import PsycopgRepository

class PsycopgEpisodeCharacterRepository(IEpisodeCharacterRepository):
    def __init__(self):
        self.manager = PsycopgRepository("episode_characters", ("id", "name"))

    def create(self, create: CreateEpisodeCharacterDTO) -> EpisodeCharacterDTO:
        data = asdict(create)
        data["id"] = self.manager.create(data)
        return EpisodeCharacterDTO(**data)
    
    def create_many(self, create: list[CreateEpisodeCharacterDTO]) -> list[EpisodeCharacterDTO]:
        data = [asdict(c) for c in create]
        ids = self.manager.create_many(data)
        return [EpisodeCharacterDTO(id = id, **d) for id, d in zip(ids, data)]
    
    def get(self, where: FindEpisodeCharacterDTO = FindEpisodeCharacterDTO()) -> list[EpisodeCharacterDTO]:
        data = asdict(where)
        response = self.manager.get(data)
        return [EpisodeCharacterDTO(**episode_character) for episode_character in response]
    
    def update(self, uuid: str, update: UpdateEpisodeCharacterDTO) -> str:
        data = asdict(update)
        response = self.manager.update(uuid, data)
        return response
    
    def delete(self, uuid: str) -> None:
        self.manager.delete(uuid)