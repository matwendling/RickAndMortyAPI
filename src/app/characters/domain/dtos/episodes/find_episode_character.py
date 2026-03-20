from dataclasses import dataclass
from typing import Optional

@dataclass
class FindEpisodeCharacterDTO:
    id: Optional[str] = None
    character_id: Optional[str] = None
    episode_id: Optional[str] = None