from framework.i_migration import IMigration
from framework.migration_provider import MigrationProvider
from migrations.history.create_tables import CreateTables

migrations_history: list[IMigration] = [
    CreateTables(),
]

migrator = MigrationProvider()
for migration in migrations_history:
    if not migrator.exists(migration.name):
        migrator.execute(
            migration.query,
            migration.params
        )
        migrator.add(migration.name)

    print(f"✅ {migration.name}")