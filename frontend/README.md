# Next.js Frontend

Frontend application for the django-nextjs full-stack project, built with Next.js and React.

## Tech Stack

- **Next.js 15** - React framework
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **App Router** - Next.js routing

## Project Structure

```
frontend/
├── src/
│   ├── app/              # App router pages
│   │   ├── layout.tsx    # Root layout
│   │   └── page.tsx      # Home page
│   └── components/       # React components (to be added)
├── public/               # Static assets
├── .gitignore
├── next.config.js        # Next.js configuration
├── package.json          # Dependencies
├── postcss.config.js     # PostCSS configuration
├── README.md
├── tailwind.config.js    # Tailwind configuration
└── tsconfig.json         # TypeScript configuration
```

## Setup

### Prerequisites

- Node.js 18+
- npm, pnpm, or yarn

### Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run development server:**
   ```bash
   npm run dev
   ```

3. **Open in browser:**
   ```
   http://localhost:3000
   ```

## Available Scripts

```bash
npm run dev        # Start development server
npm run build      # Build for production
npm run start      # Start production server
npm run lint       # Run ESLint
```

## Configuration

### Environment Variables

Create a `.env.local` file in the frontend directory:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api
```

- `NEXT_PUBLIC_API_URL` - Backend API base URL (Django Ninja endpoints at `/api/`)

## Connecting to Django Backend

The frontend will communicate with the Django backend API at `http://127.0.0.1:8000`. Make sure the backend server is running before making API calls.

## Development

- Development server: `http://localhost:3000`
- Hot module replacement enabled
- TypeScript strict mode enabled
- Tailwind CSS for styling

## Notes

- Uses Next.js App Router (not Pages Router)
- TypeScript is configured for strict type checking
- Tailwind CSS utility classes available globally
- API calls will be made to Django Ninja endpoints (to be implemented)