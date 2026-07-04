# Template: Makefile (Common development tasks)
# Usage: Run `make <target>`

.PHONY: help dev build test lint format clean docker-up docker-down db-migrate

help:
	@echo "MyApp Makefile Commands"
	@echo "======================="
	@echo "make dev              - Start development server"
	@echo "make build            - Build TypeScript"
	@echo "make test             - Run tests"
	@echo "make test-watch       - Run tests in watch mode"
	@echo "make coverage         - Generate test coverage"
	@echo "make lint             - Run ESLint"
	@echo "make lint-fix         - Fix ESLint issues"
	@echo "make format           - Format code with Prettier"
	@echo "make format-check     - Check formatting"
	@echo "make clean            - Clean build artifacts"
	@echo "make docker-up        - Start Docker services"
	@echo "make docker-down      - Stop Docker services"
	@echo "make db-migrate       - Run database migrations"
	@echo "make db-seed          - Seed database"
	@echo "make db-reset         - Reset database"
	@echo "make ci               - Run CI checks (lint + test + coverage)"

dev:
	npm run dev

build:
	npm run build

test:
	npm test

test-watch:
	npm run test:watch

coverage:
	npm run test:coverage

lint:
	npm run lint

lint-fix:
	npm run lint:fix

format:
	npm run format

format-check:
	npm run format:check

clean:
	rm -rf dist/ coverage/ node_modules/

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f web

db-migrate:
	npm run db:migrate

db-seed:
	npm run db:seed

db-reset:
	npm run db:reset

ci: lint test coverage
	@echo "✓ All CI checks passed"

setup: install db-migrate
	@echo "✓ Setup complete"

install:
	npm install

dev-setup: install docker-up db-migrate
	@echo "✓ Development setup complete"
	@echo "Start dev server with: make dev"
