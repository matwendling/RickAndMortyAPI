from dataclasses import dataclass

@dataclass
class EpisodeDTO:
    id: str
    name: str
    num: int
    season: int