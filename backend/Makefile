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

help:
	@echo ""
	@echo "Available make commands:"
	@echo "  make help             			- Show this help message."
	@echo "  make run              			- Starts the Django dev server and exposes it to the local network."
	@echo "  make migrations       			- Creates new Django database migrations."
	@echo "  make migrate          			- Applies database migrations to the database."
	@echo "  make superuser        			- Creates a Django superuser account."
	@echo "  make collectstatic    			- Collects static files for deployment."