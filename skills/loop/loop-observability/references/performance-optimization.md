# Performance Optimization Guide

## Frontend Performance

### Critical Metrics (Web Vitals)
- LCP (Largest Contentful Paint): < 2.5s
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1

### Optimization Techniques
```javascript
// 1. Code Splitting
const UserList = lazy(() => import('./UserList'));

// 2. Memoization
const MemoUser = memo(UserComponent);

// 3. Lazy Loading
<Image src="..." loading="lazy" />

// 4. Compression
// Enable gzip in webpack/server

// 5. Caching
// Set Cache-Control headers
response.set('Cache-Control', 'public, max-age=3600');
```

## Backend Performance

### Query Optimization
```sql
-- Bad: N+1 query
SELECT * FROM users;
// Then loop: SELECT * FROM posts WHERE user_id = ?

-- Good: JOIN query
SELECT u.*, p.* FROM users u
LEFT JOIN posts p ON u.id = p.user_id;

-- Use indexes
CREATE INDEX idx_user_id ON posts(user_id);
```

### Caching Strategy
```javascript
// 1. In-Memory Cache
const cache = new Map();

// 2. Redis Cache
await redis.set('user:123', JSON.stringify(user), 'EX', 3600);

// 3. Database Query Cache
SELECT * FROM users WHERE id = 123; // Will cache
```

### Connection Pooling
```javascript
// PostgreSQL
const pool = new Pool({
  max: 20,
  connectionTimeoutMillis: 2000,
  idleTimeoutMillis: 30000,
});
```

## Database Performance

### Indexes
```sql
-- Single column
CREATE INDEX idx_email ON users(email);

-- Composite
CREATE INDEX idx_user_status ON users(user_id, status);

-- Partial (faster)
CREATE INDEX idx_active_users ON users(id) 
WHERE status = 'active';
```

### Query Analysis
```sql
-- Explain plan
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@example.com';

-- Check index usage
SELECT schemaname, tablename, indexname 
FROM pg_indexes 
WHERE schemaname NOT IN ('pg_catalog', 'information_schema');
```

## Monitoring

### Key Metrics
- Response time: target < 200ms
- Database query time: target < 50ms
- Cache hit ratio: target > 80%
- Error rate: target < 0.1%

### Tools
- DataDog, New Relic, Prometheus
- APM (Application Performance Monitoring)
- Real User Monitoring (RUM)
