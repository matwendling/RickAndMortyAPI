from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateCharacterDTO:
    name: Optional[str] = None
    status: Optional[str] = None
    image: Optional[bytes] = None
    specie_id: Optional[str] = None
    type_id: Optional[str] = None
    gender: Optional[str] = None
    origin_id: Optional[str] = None
    location_id: Optional[str] = None