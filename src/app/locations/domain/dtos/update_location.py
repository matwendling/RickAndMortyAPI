from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateLocationDTO:
    name: Optional[str] = None