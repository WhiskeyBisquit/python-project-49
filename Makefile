install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-instal-to-venv: # install package to virtual environment
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8 brain_games
