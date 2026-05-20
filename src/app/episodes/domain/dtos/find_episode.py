from dataclasses import dataclass
from typing import Optional

@dataclass
class FindEpisodeDTO:
    id: Optional[str] = None
    name: Optional[str] = None
    num: Optional[int] = None
    season: Optional[int] = None