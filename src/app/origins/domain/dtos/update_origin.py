from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateOriginDTO:
    name: Optional[str] = None