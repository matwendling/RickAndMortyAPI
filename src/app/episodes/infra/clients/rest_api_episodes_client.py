import requests

from app.episodes.domain.clients.i_episode_client import IEpisodeClient
from app.episodes.domain.dtos.episodes_client.episode_client_dto import EpisodeClientDTO


class RestAPIEpisodesClient(IEpisodeClient):
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/episode"

    def fetch_one(self, id: str) -> EpisodeClientDTO:
        url = f"{self.url}/{id}"
        res = requests.get(url).json()
        return self.__serializer_one(res)
    
    def fetch_all(self) -> list[EpisodeClientDTO]:
        episodes_count = requests.get(self.url).json()["info"]["count"]
        episodes_num = [f"{a}" for a in range(0, episodes_count)]
        url = self.url + "/" + ",".join(episodes_num)
        response = requests.get(url).json()
        return [self.__serializer_one(res) for res in response]
        
    def fetch_many(self, quant: list[str]) -> list[EpisodeClientDTO]:
        url = f"{self.url}/"

        for p in quant:
            url += f"{p}, "
        
        if url.endswith(", "):
            url = url.removesuffix(", ")

        res = requests.get(url).json()
        return [self.__serializer_one(d) for d in res]

    def __serializer_one(self, data: dict) -> EpisodeClientDTO:
        episode_data = data["episode"]
        episode_index = episode_data.index("E")
        season = episode_data[1:episode_index]
        episode = episode_data[episode_index+1:]

        return EpisodeClientDTO(
            name=data["name"],
            season=int(season),
            num=int(episode)
        )