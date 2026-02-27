from dataclasses import dataclass

@dataclass
class CreateCharacterDTO:
    name: str
    status: str
    specie_id: str
    type_id: str
    gender: str
    origin_id: str
    location_id: str