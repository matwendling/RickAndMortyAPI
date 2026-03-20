from app.characters.domain.dtos.create_character import CreateCharacterDTO
from app.characters.infra.repositories.psycopg_character_repository import PsycopgCharacterRepository
from app.locations.domain.dtos.create_location import CreateLocationDTO
from app.locations.domain.dtos.find_location import FindLocationDTO
from app.locations.domain.dtos.update_location import UpdateLocationDTO
from app.locations.infra.repositories.psycopg_location_repository import PsycopgLocationRepository

repo = PsycopgLocationRepository()

for found in repo.get():
    repo.delete(found.id)

gettwo = repo.get()
print(gettwo)