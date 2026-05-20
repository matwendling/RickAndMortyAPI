from typing import Optional

from pydantic import BaseModel

class FindEpisodeRequest(BaseModel):
    url: Optional[str] = None
    num: Optional[int] = None
    season: Optional[int] = None