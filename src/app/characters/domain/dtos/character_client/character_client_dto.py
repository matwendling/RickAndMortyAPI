from dataclasses import dataclass
import json

@dataclass
class CharacterClientDTO:
    id: str
    name: str
    status: str
    specie: str
    character_type: str
    gender: str
    origin: str
    location: str
    episodes: list[str]
    image: str

    def __str__(self) -> str:
        
        obj = {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "specie": self.specie,
            "character_type": self.character_type,
            "gender": self.gender,
            "origin": self.origin,
            "location": self.location,
            "episodes": self.episodes,
            "image": self.image
        } 
        return json.dumps(obj, indent=3)