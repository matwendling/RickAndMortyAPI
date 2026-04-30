from app.characters.domain.dtos.character import CharacterDTO
from app.characters.domain.dtos.create_character import CreateCharacterDTO
from app.characters.domain.dtos.episodes.create_episode_character import CreateEpisodeCharacterDTO
from app.characters.domain.dtos.episodes.find_episode_character import FindEpisodeCharacterDTO
from app.characters.domain.dtos.episodes.update_episode_character import UpdateEpisodeCharacterDTO
from app.characters.infra.repositories.psycopg_character_repository import PsycopgCharacterRepository
from app.characters.infra.repositories.psycopg_episode_character_repository import PsycopgEpisodeCharacterRepository
from app.classification_types.domain.dtos.create_classification_type import CreateClassificationTypeDTO
from app.classification_types.domain.dtos.find_classification_type import FindClassificationTypeDTO
from app.classification_types.domain.dtos.update_classification_type import UpdateClassificationTypeDTO
from app.classification_types.infra.repositories.psycopg_classification_type import PsycopgClassificationTypeRepository
from app.episodes.domain.dtos.create_episode import CreateEpisodeDTO
from app.episodes.domain.dtos.find_episode import FindEpisodeDTO
from app.episodes.domain.dtos.update_episode import UpdateEpisodeDTO
from app.episodes.infra.repositories.psycopg_episode_repository import PsycopgEpisodeRepository
from app.locations.domain.dtos.create_location import CreateLocationDTO
from app.locations.domain.dtos.find_location import FindLocationDTO
from app.locations.domain.dtos.update_location import UpdateLocationDTO
from app.locations.infra.repositories.psycopg_location_repository import PsycopgLocationRepository
from app.origins.domain.dtos.create_origin import CreateOriginDTO
from app.origins.domain.dtos.find_origin import FindOriginDTO
from app.origins.domain.dtos.update_origin import UpdateOriginDTO
from app.origins.infra.repositories.psycopg_origin_repository import PsycopgOriginRepository
from app.species.domain.dtos.create_specie import CreateSpecieDTO
from app.species.domain.dtos.find_specie import FindSpecieDTO
from app.species.domain.dtos.update_specie import UpdateSpecieDTO
from app.species.infra.repositories.psycopg_specie_repository import PsycopgSpecieRepository

repo = PsycopgLocationRepository()

# for found in repo.get():
#     repo.delete(found.id)

# gettwo = repo.get()
# print(gettwo)

## CHARACTER TEST

img = open("/home/kurtwendling/Documents/Programação/dev/RickAndMortyAPI/pato.png", "rb")

character_repo = PsycopgCharacterRepository()
character = CreateCharacterDTO(
    "Mateta",
    "alive",
    "93e4aa60-7ee6-4136-8f7e-4629118c6cfc",
    "f67ea66b-5897-40ad-b020-476b4b30e330",
    "male",
    "2755b802-c420-41bc-9d7e-5226a9ade8d2",
    "bc664c2d-028e-4eb2-9a72-823ed7b42aa4",
    img,
    "1"
)

character2 = CharacterDTO
breakpoint()

#character_repo.create(character)

# ------------------------------------------------------------ 

## CLASSIFICATION TYPES TEST
 
classification_type_repo = PsycopgClassificationTypeRepository()
classification_type = CreateClassificationTypeDTO("Test 2")
classification_type_finder = FindClassificationTypeDTO(name="Test")
classification_type_updater = UpdateClassificationTypeDTO(name="Test 1")

classification_type_repo.create(classification_type)

print(classification_type_repo.get(classification_type_finder))
classification_type_repo.update("f67ea66b-5897-40ad-b020-476b4b30e330", classification_type_updater)
print(classification_type_repo.get())
print("="*60)

# ------------------------------------------------------------ 

## EPISODES TEST

episode_repo = PsycopgEpisodeRepository()
episode = CreateEpisodeDTO("abcdefg.com", 2, 2)
episode_finder = FindEpisodeDTO(url="abcdefg")
episode_updater = UpdateEpisodeDTO(num=2, season=1)

episode_repo.create(episode)

print(episode_repo.get())
episode_repo.update("07b42e30-1a0f-452d-a646-0278a3b11c27", episode_updater)
print(episode_repo.get())
print("="*60)

# ------------------------------------------------------------ 

## LOCATIONS TEST

location_repo = PsycopgLocationRepository()
location = CreateLocationDTO("Plerth")
location_finder = FindLocationDTO()
location_updater = UpdateLocationDTO(name="Eerth")

location_repo.create(location)

print(location_repo.get())
location_repo.update("8fbde64b-1412-4835-add1-88b9997d7d68", location_updater)
print(location_repo.get())
print("="*60)

# ------------------------------------------------------------ 

## ORIGINS TEST

origin_repo = PsycopgOriginRepository()
origin = CreateOriginDTO("Eerth")
origin_finder = FindOriginDTO()
origin_updater = UpdateOriginDTO(name="Earth")

origin_repo.create(origin)

print(origin_repo.get())
origin_repo.update("2755b802-c420-41bc-9d7e-5226a9ade8d2", origin_updater)
print(origin_repo.get())
print("="*60)

# ------------------------------------------------------------ 

## SPECIES TEST

specie_repo = PsycopgSpecieRepository()
specie = CreateSpecieDTO("Human")
specie_finder = FindSpecieDTO()
specie_updater = UpdateSpecieDTO(name="Slime")

specie_repo.create(specie)

print(specie_repo.get())
specie_repo.update("b6c27998-a879-47af-8ac6-7535260dea68", specie_updater)
print(specie_repo.get())
print("="*60)

# ------------------------------------------------------------ 

## EPISODES CHARACTER TEST
episodes_characters_repo = PsycopgEpisodeCharacterRepository()
episode_character = CreateEpisodeCharacterDTO("", "07b42e30-1a0f-452d-a646-0278a3b11c27")
episode_character_finder = FindEpisodeCharacterDTO()
episode_character_updater = UpdateEpisodeCharacterDTO()

episodes_characters_repo.create(episode_character)

print(episodes_characters_repo.get())
episodes_characters_repo.update("", episode_character_updater)
print(episodes_characters_repo.get())
print("="*60)