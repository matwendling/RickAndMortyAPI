from framework.i_migration import IMigration

class CreateTables(IMigration):
    name = "create_database_tables"

    @property
    def query(self) -> str:
        return """
        -- ============================================
        -- EXTENSÃO PARA UUID
        -- ============================================
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

        -- ============================================
        -- CRIAÇÃO DOS TIPOS ENUM
        -- ============================================
        CREATE TYPE character_status AS ENUM ('alive', 'dead', 'unknown');

        CREATE TYPE character_gender AS ENUM ('female', 'male', 'genderless', 'unknown');

        -- ============================================
        -- TABELA: episodes
        -- ============================================
        CREATE TABLE episodes (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            url VARCHAR(255) NOT NULL,
            num INT NOT NULL,
            season INT NOT NULL,

            CONSTRAINT unique_episode_row UNIQUE (url, num, season)
        );

        -- ============================================
        -- TABELA: classification_types
        -- ============================================
        CREATE TABLE classification_types (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(255) NOT NULL,

            CONSTRAINT unique_classification_type_row UNIQUE (name)
        );

        -- ============================================
        -- TABELA: species
        -- ============================================
        CREATE TABLE species (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(255) NOT NULL,

            CONSTRAINT unique_species_row UNIQUE (name)
        );

        -- ============================================
        -- TABELA: locations
        -- ============================================
        CREATE TABLE locations (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(255) NOT NULL,

            CONSTRAINT unique_location_row UNIQUE (name)
        );

        -- ============================================
        -- TABELA: origins
        -- ============================================
        CREATE TABLE origins (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(255) NOT NULL,

            CONSTRAINT unique_origin_row UNIQUE (name)
        );

        -- ============================================
        -- TABELA: characters
        -- ============================================
        CREATE TABLE characters (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(255) NOT NULL,
            status character_status NOT NULL,
            specie_id UUID NOT NULL,
            type_id UUID NOT NULL,
            gender character_gender NOT NULL,
            origin_id UUID NOT NULL,
            location_id UUID NOT NULL,
            image BYTEA,
            api_id INT,

            CONSTRAINT fk_specie
                FOREIGN KEY (specie_id)
                REFERENCES species(id),

            CONSTRAINT fk_type
                FOREIGN KEY (type_id)
                REFERENCES classification_types(id),

            CONSTRAINT fk_origin
                FOREIGN KEY (origin_id)
                REFERENCES origins(id),

            CONSTRAINT fk_location
                FOREIGN KEY (location_id)
                REFERENCES locations(id),

            CONSTRAINT unique_character_row UNIQUE (
                name,
                status,
                specie_id,
                type_id,
                gender,
                origin_id,
                location_id,
                image,
                api_id
            )
        );

        -- ============================================
        -- TABELA: episodes_characters
        -- ============================================
        CREATE TABLE episodes_characters (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            character_id UUID NOT NULL,
            episode_id UUID NOT NULL,

            CONSTRAINT fk_character
                FOREIGN KEY (character_id)
                REFERENCES characters(id)
                ON DELETE CASCADE,

            CONSTRAINT fk_episode
                FOREIGN KEY (episode_id)
                REFERENCES episodes(id)
                ON DELETE CASCADE,

            CONSTRAINT unique_episode_character_row UNIQUE (character_id, episode_id)
        );
        """
    
    @property
    def params(self) -> list:
        return []