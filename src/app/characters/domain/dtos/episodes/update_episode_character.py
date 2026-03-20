from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateEpisodeCharacterDTO:
    character_id: Optional[str] = None
    episode_id: Optional[str] = None