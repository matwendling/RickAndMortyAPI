from app.episodes.domain.dtos.episodes_client.episodes_client_dto import EpisodesClientDTO

class IEpisodesClient:
    def fetch_one(self, id: str) -> EpisodesClientDTO:
        """
        """

    def fetch_all(self) -> list[EpisodesClientDTO]:
        """
        """

    def fetch_many(self, quant: list[str]) -> list[EpisodesClientDTO]:
        """
        """