run:
	cd ./src && poetry run python -m main

migrate:
	echo "pato e pata running the migrations from now on >:/"
	cd ./src && poetry run python -m migrations.migrate
# && allows you to insert more then one command on the same line 
# the first changes directory (cd) and the other executes (exec)