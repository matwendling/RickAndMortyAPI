from app.characters.domain.clients.i_character_client import ICharacterClient
from app.characters.domain.dtos.character_client.character_client_dto import CharacterClientDTO
import requests

class RestAPICharacterClient(ICharacterClient):
    def __init__(self):
        self.url = "https://rickandmortyapi.com/api/character"

    def fetch_one(self, id: str) -> CharacterClientDTO:
        url = f"{self.url}/{id}"
        res = requests.get(url).json()
        return self.__serializer_one(res)
        
    def fetch_all(self) -> list[CharacterClientDTO]:
        res = requests.get(self.url).json()["results"]
        return [self.__serializer_one(d) for d in res]

    def fecth_many(self, quant: list[str]) -> list[CharacterClientDTO]:
        url = f"{self.url}/"

        for p in quant:
            url += f"{p}, "

        if url.endswith(", "):
            url = url.removesuffix(", ")

        res = requests.get(url).json()
        return [self.__serializer_one(d) for d in res]

    def __serializer_one(self, data: dict) -> CharacterClientDTO:
        episodes = [
            e.removeprefix("https://rickandmortyapi.com/api/episode/") 
            for e in data["episode"]
        ]
        image = requests.get(data["image"]).content
        return CharacterClientDTO(
            id=data["id"],
            name=data["name"],
            status=data["status"],
            specie=data["species"],
            character_type=data["type"],
            gender=data["gender"],
            origin=data["origin"]["name"],
            location=data["location"]["name"],
            episodes=episodes,
            image=image,
        )