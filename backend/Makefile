.PHONY: help run migrations migrate superuser collectstatic clean-mac clean-windows

run:
	uv run python manage.py runserver 0.0.0.0:8000

migrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

superuser:
	uv run python manage.py createsuperuser

collectstatic:
	uv run python manage.py collectstatic --no-input

clean-mac:
	find . -type f \( -name "*.py[co]" -o -name ".DS_Store" \) -delete
	find . -type d -name "__pycache__" -delete

clean-windows:
	python -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__') if '.venv' not in p.parts]"

help:
	@echo ""
	@echo "Available make commands:"
	@echo "  make help             			- Show this help message."
	@echo "  make run              			- Starts the Django dev server and exposes it to the local network."
	@echo "  make migrations       			- Creates new Django database migrations."
	@echo "  make migrate          			- Applies database migrations to the database."
	@echo "  make superuser        			- Creates a Django superuser account."
	@echo "  make collectstatic    			- Collects static files for deployment."
	@echo "  make clean-(mac/windows)       - Removes all build artifacts"