from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateEpisodeDTO:
    url: Optional[str] = None
    num: Optional[int] = None
    season: Optional[int] = None