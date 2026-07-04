# Multi-stage Dockerfile (Node.js Application)
# Usage: Build & run containerized application
# Build: docker build -t app:latest .
# Run: docker run -p 3000:3000 app:latest

# Stage 1: BUILDER (Dependencies + Build)
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm ci --only=production && \
    npm cache clean --force

# Copy source code
COPY . .

# Build application (if needed)
RUN npm run build || true

# Stage 2: RUNTIME (Minimal production image)
FROM node:18-alpine

WORKDIR /app

# Security: Run as non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Copy from builder
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/package*.json ./

# Set environment
ENV NODE_ENV=production
ENV PORT=3000

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/health', (r) => {if (r.statusCode !== 200) throw new Error(r.statusCode)})"

# Switch to non-root user
USER nodejs

# Start application
CMD ["node", "dist/index.js"]

# NOTES
# - Multi-stage: smaller final image
# - Alpine: 5MB base vs 900MB full Node
# - Non-root user: security best practice
# - Health check: K8s/Docker monitoring
# - Only production deps in final image
