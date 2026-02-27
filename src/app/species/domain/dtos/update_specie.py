from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateSpecieDTO:
    name: Optional[str] = None