from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateClassificationTypeDTO:
    name: Optional[str]