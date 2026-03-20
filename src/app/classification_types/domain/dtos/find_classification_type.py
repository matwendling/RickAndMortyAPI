from dataclasses import dataclass
from typing import Optional

@dataclass
class FindClassificationTypeDTO:
    id: Optional[str] = None 
    name: Optional[str] = None