from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateCharacterDTO:
    name: Optional[str] = None
    status: Optional[str] = None
    image: Optional[bytes] = None