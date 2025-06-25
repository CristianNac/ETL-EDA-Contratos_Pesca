#Ayuda
.PHONY: help clean lint etl

help:
	@echo "Tareas disponibles"
	@echo "make clean  ->   Borra cache de python y ruff"
	@echo "make lint   ->   Revision del codigo con ruff"
	@echo "make etl    ->   Carga la data desde el csv a postgresql"

clean:
	@echo "Limpiando caches"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .ruff_cache

lint:
	@echo "Ejecutando ruff"
	poetry run ruff check src
	
etl: clean
	@echo "Ejecutando carga de datos.."
	PYTHONPATH=src poetry run python -m ETL.extract
