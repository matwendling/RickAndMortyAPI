from typing import Optional

from pydantic import BaseModel

class FindCharacterRequest(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    specie_id: Optional[str] = None
    type_id: Optional[str] = None
    gender: Optional[str] = None
    origin_id: Optional[str] = None
    location_id: Optional[str] = None
    image: Optional[bytes] = None
    api_id: Optional[str] = None