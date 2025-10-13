# Django Backend

Backend API of the full-stack application, built with Django and Django Ninja.

## Tech Stack

- **Python 3.13+**
- **Django 5.27+** - Backend framework
- **Django Ninja** - REST API framework
- **PostgreSQL** - Database
- **UV** - Package manager
- **Django Unfold** - Modern admin interface
- **python-decouple** - Environment variable management

## Project Structure

```
backend/
├── config/
│   ├── components/
│   │   ├── __init__.py
│   │   └── unfold.py      # Unfold admin configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Main Django settings
│   ├── urls.py
│   └── wsgi.py
├── .env                   # Environment variables (not committed)
├── .env.example           # Environment template
├── .gitignore
├── Makefile               # Task runner commands
├── manage.py
├── pyproject.toml         # Python dependencies
├── README.md
└── uv.lock                # UV lockfile
```

## Setup

### Prerequisites

- Python 3.13+
- PostgreSQL
- [UV package manager](https://github.com/astral-sh/uv)
- Make (macOS/Linux) or [Make for Windows](https://gnuwin32.sourceforge.net/packages/make.htm)

### Installation

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env

   # Edit .env with your database credentials and relevant settings
   ```

3. **Run migrations:**
   ```bash
   make migrate
   ```

4. **Create superuser:**
   ```bash
   make superuser
   ```

5. **Run development server:**
   ```bash
   make run
   ```

Server will be available at `http://127.0.0.1:8000`

## Available Commands

```bash
make help                # Show all available commands
make run                 # Run dev server (exposes to local network)
make migrations          # Create new migrations
make migrate             # Apply migrations
make superuser           # Create superuser
make collectstatic       # Collect static files
make clean-mac           # Remove Python cache (macOS/Linux)
make clean-windows       # Remove Python cache (Windows)
```

## Environment Variables

See `.env.example` for required variables:

### Database Configurations
- `DATABASE_DEV` - Development database URL (e.g., `postgres://user:pass@localhost:5432/dbname`)
- `DATABASE_PROD` - Production database URL

### Django Core Settings
- `SECRET_KEY` - Django secret key (auto-generated in DEBUG mode if not set)
- `DEBUG` - Debug mode (`True`/`False`)
- `ALLOWED_HOSTS` - Comma-separated allowed hosts (e.g., `127.0.0.1,localhost`)

### Production Settings
- `STATIC_ROOT` - Static files directory for production (e.g., `/var/www/static/`)
- `CSRF_TRUSTED_ORIGINS` - Comma-separated trusted origins for CSRF (e.g., `https://example.com`)

## Development

- Admin interface: `http://127.0.0.1:8000/admin`
- API documentation: (to be added with Django Ninja)

## Configuration Details

### Timezone & Internationalization
- **Timezone:** Asia/Manila
- **Language:** English (en-us)
- Internationalization (i18n) enabled

### Static & Media Files
- **Static URL:** `/static/`
- **Static Root:** `staticfiles/` (dev) or configured path (prod)
- **Media URL:** `/media/`
- **Media Root:** `media/`

### Security Features
- CSRF protection enabled
- Session-based authentication
- Secure password validation (similarity, length, common passwords, numeric checks)
- Auto-generates SECRET_KEY in development mode