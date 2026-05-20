run:
	cd ./src && poetry run python -m main

migrate:
	echo "pato e pata running the migrations from now on >:/"
	cd ./src && poetry run python -m migrations.migrate
# && allows you to insert more then one command on the same line 
# the first changes directory (cd) and the other executes (exec)

_reset_db:
	psql -d postgres -U kurtwendling -c "DROP DATABASE IF EXISTS rickandmortyapi;"
	psql -d postgres -U kurtwendling -c "CREATE DATABASE rickandmortyapi;"

reset_db: _reset_db migrate