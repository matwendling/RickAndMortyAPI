from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateSpecieDTO:
    id: Optional[str] = None
    name: Optional[str] = None