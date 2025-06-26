#Ayuda
.PHONY: help clean lint extract

help:
	@echo "Tareas disponibles"
	@echo "make clean      ->   Borra cache de python y ruff"
	@echo "make lint       ->   Revision del codigo con ruff"
	@echo "make extract    ->   Carga la data desde los csv"
	@echo "make transform  ->   Carga y transforma la data"

clean:
	@echo "Limpiando caches"
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .ruff_cache

lint:
	@echo "Ejecutando ruff"
	poetry run ruff check src
	
extract: clean
	@echo "Ejecutando carga de datos.."
	PYTHONPATH=src poetry run python -m ETL.extract

transform: clean
	@echo "Ejecutando la carga y transformacion de datos.."
	PYTHONPATH=src poetry run python -m ETL.transform
