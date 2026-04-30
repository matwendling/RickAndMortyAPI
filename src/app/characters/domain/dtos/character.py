from dataclasses import dataclass

@dataclass
class CharacterDTO:
    id: str
    name: str
    status: str
    specie_id: str
    type_id: str
    gender: str
    origin_id: str
    location_id: str
    image: bytes
    api_id: str