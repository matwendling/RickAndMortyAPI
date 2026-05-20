from abc import ABC, abstractmethod

from app.episodes.domain.dtos.episodes_client.episode_client_dto import EpisodeClientDTO

class IEpisodeClient(ABC):

    @abstractmethod
    def fetch_one(self, id: str) -> EpisodeClientDTO:
        """
        """

    @abstractmethod
    def fetch_all(self) -> list[EpisodeClientDTO]:
        """
        """

    @abstractmethod
    def fetch_many(self, quant: list[str]) -> list[EpisodeClientDTO]:
        """
        """