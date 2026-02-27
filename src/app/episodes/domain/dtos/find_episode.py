from dataclasses import dataclass
from typing import Optional

@dataclass
class FindEpisodeDTO:
    id: Optional[str] = None
    url: Optional[str] = None
    num: Optional[int] = None
    season: Optional[int] = None