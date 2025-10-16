# Django + Next.js Full-Stack Application

A modern full-stack web application built with Django REST API backend and Next.js frontend.

## Project Structure

```
django-nextjs/
├── .vscode/
│   └── settings.json   # VSCode workspace settings
├── backend/            # Django REST API
│   ├── config/        # Django project configuration
│   ├── manage.py
│   └── README.md      # Backend-specific documentation
├── frontend/          # Next.js application
│   ├── src/          # Source code
│   ├── public/       # Static assets
│   └── README.md     # Frontend-specific documentation
├── .gitignore        # Root gitignore (OS files)
├── Makefile          # Global task runner
└── README.md
```

## Tech Stack

### Backend
- **Django 5.27+** with **Django Ninja** for REST API
- **PostgreSQL** database
- **UV** package manager
- **Django Unfold** admin interface

### Frontend
- **Next.js 15** with **App Router**
- **React 19**
- **Tailwind CSS** for styling

## Quick Start

### Prerequisites

- Python 3.13+
- Node.js 18+
- PostgreSQL
- [UV package manager](https://github.com/astral-sh/uv)
- Make (for task runner)

### Setup Both Projects

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cymophic/django-nextjs.git

   cd django-nextjs
   ```

2. **Backend Setup:**
   ```bash
   cd backend

   uv sync

   cp .env.example .env
   # Edit .env with your database credentials

   make migrate

   make superuser
   ```

3. **Frontend Setup:**
   ```bash
   cd ../frontend

   npm install

   cp .env.example .env.local
   # Edit .env.local if needed (default points to localhost:8000)
   ```

### Running Development Servers

**Terminal 1 (Backend):**
```bash
cd backend

make run
```

**Terminal 2 (Frontend):**
```bash
cd frontend

npm run dev
```

### Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000/api/
- **Django Admin:** http://localhost:8000/{ADMIN_URL} (default: /admin)

## Documentation

- [Backend Documentation](./backend/README.md) - Django setup, API endpoints, database configuration
- [Frontend Documentation](./frontend/README.md) - Next.js setup, component structure, styling

## Development Workflow

1. **Backend changes:** Work in `backend/` directory
   - API endpoints with Django Ninja
   - Database models and migrations
   - Admin interface customization

2. **Frontend changes:** Work in `frontend/` directory
   - React components in `src/components/`
   - Pages in `src/app/`
   - API calls to Django backend

3. **Environment variables:**
   - Backend: `backend/.env`
   - Frontend: `frontend/.env.local`

## Available Commands

### Root Commands
```bash
make help              # Show available global commands
make clean-mac         # Clean Python cache (macOS/Linux)
make clean-windows     # Clean Python cache (Windows)
make repo-labels       # View all GitHub labels for this repo (requires GitHub CLI)
```

### Backend Commands (from backend/)
```bash
make help             # Show backend commands
make run              # Start Django dev server
make migrate          # Run database migrations
make migrations       # Create new migrations
make superuser        # Create admin user
make collectstatic    # Collect static files
```

### Frontend Commands (from frontend/)
```bash
npm run dev          # Start Next.js dev server (with Turbopack)
npm run build        # Build for production (with Turbopack)
npm run start        # Start production server
```

## Project Goals

This is a practice project focused on:
- Building production-ready full-stack applications
- Following industry conventions and best practices
- Implementing modern development workflows
- Separating concerns between backend and frontend

## Notes

- Backend uses Neon PostgreSQL for database
- Frontend uses Next.js App Router (not Pages Router)
- API communication via Django Ninja REST endpoints
- Environment-based configuration for dev/prod separation