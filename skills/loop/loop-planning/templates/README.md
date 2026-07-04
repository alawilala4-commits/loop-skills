# Project README Template
# Usage: Copy to root, fill in your project details, customize sections

# MyApp — [Brief Description]

Production-ready Node.js application with TypeScript, PostgreSQL, Redis, and Docker.

## Features

✅ Type-safe TypeScript codebase
✅ REST API with Express
✅ PostgreSQL database with migrations
✅ Redis caching layer
✅ Docker & Docker Compose setup
✅ GitHub Actions CI/CD
✅ Comprehensive test coverage
✅ ESLint & Prettier formatting
✅ Production-ready deployment

## Tech Stack

- **Runtime**: Node.js 18+
- **Language**: TypeScript
- **Framework**: Express.js
- **Database**: PostgreSQL 15
- **Cache**: Redis 7
- **Testing**: Jest + Supertest
- **Linting**: ESLint + Prettier
- **CI/CD**: GitHub Actions
- **Container**: Docker & Docker Compose

## Quick Start

### Prerequisites
- Node.js 18+
- Docker & Docker Compose (optional)
- PostgreSQL 15 (or use Docker)

### Setup (Local)

```bash
# 1. Clone repository
git clone <repo-url>
cd myapp

# 2. Install dependencies
npm install

# 3. Setup environment
cp .env.example .env
# Edit .env with your values

# 4. Run database migrations
npm run db:migrate

# 5. Start development server
npm run dev

# Visit http://localhost:3000
```

### Setup (Docker)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f web

# Stop services
docker-compose down
```

## Commands

```bash
# Development
npm run dev          # Start dev server with hot-reload
npm run build        # Build TypeScript
npm start            # Start production server

# Testing
npm test             # Run tests
npm run test:watch   # Watch mode
npm run test:coverage # With coverage report

# Code Quality
npm run lint         # ESLint check
npm run lint:fix     # Auto-fix issues
npm run format       # Prettier format
npm run format:check # Check formatting

# Database
npm run db:migrate   # Run migrations
npm run db:seed      # Seed test data
npm run db:reset     # Reset database

# Docker
docker-compose up -d # Start services
docker-compose down  # Stop services
docker-compose logs  # View logs
```

## Project Structure

```
.
├── src/
│   ├── api/          # Express routes
│   ├── models/       # Database models
│   ├── services/     # Business logic
│   ├── middleware/   # Express middleware
│   ├── utils/        # Utility functions
│   └── index.ts      # Application entry
├── tests/            # Test files
├── scripts/          # Migration scripts
├── .github/
│   └── workflows/    # GitHub Actions
├── docker-compose.yml
├── Dockerfile
├── tsconfig.json
├── .eslintrc.json
├── .prettierrc
└── package.json
```

## API Documentation

### Health Check
```bash
GET /health
Response: { "status": "ok" }
```

### Users Endpoint
```bash
# Get all users
GET /api/users

# Get user by ID
GET /api/users/:id

# Create user
POST /api/users
Body: { "name": "...", "email": "..." }

# Update user
PUT /api/users/:id
Body: { "name": "..." }

# Delete user
DELETE /api/users/:id
```

## Testing

```bash
# Run all tests
npm test

# Run specific test file
npm test -- user.test.ts

# Watch mode
npm run test:watch

# Coverage report
npm run test:coverage
```

## Deployment

### Staging
```bash
git push origin develop  # Triggers CI/CD
# GitHub Actions runs tests → builds Docker image → deploys to staging
```

### Production
```bash
git tag v1.0.0
git push origin v1.0.0  # Triggers production deployment
```

## Environment Variables

See `.env.example` for all available variables:
- `NODE_ENV` - development/production
- `DATABASE_URL` - PostgreSQL connection
- `REDIS_URL` - Redis connection
- `API_PORT` - Server port

## Troubleshooting

**Port 3000 already in use?**
```bash
lsof -i :3000
kill -9 <PID>
```

**Database connection error?**
```bash
npm run db:migrate  # Run migrations
docker-compose restart db  # Restart container
```

**Tests failing?**
```bash
npm run test:watch  # Debug mode
npm run test -- --verbose
```

## Contributing

1. Create feature branch: `git checkout -b feature/name`
2. Make changes & commit: `git commit -m "feat: description"`
3. Push to branch: `git push origin feature/name`
4. Open Pull Request

## Code Style

- ESLint: Configured in `.eslintrc.json`
- Prettier: Configured in `.prettierrc`
- Run before commit: `npm run lint:fix && npm run format`

## License

MIT License - see LICENSE file

## Support

- Issues: GitHub Issues
- Discussions: GitHub Discussions
- Slack: #engineering channel
