# Debugging Strategies & Techniques

## Systematic Debugging Process

### Step 1: Reproduce the Issue
- Get clear reproduction steps
- Document inputs & outputs
- Check if issue is intermittent or consistent
- Isolate the component/function

### Step 2: Collect Information
```bash
# Logs
tail -f logs/app.log
docker-compose logs -f web

# System info
node -v
npm -v
process.env

# Database state
SELECT * FROM users WHERE id = 123;
```

### Step 3: Form Hypotheses
- "Bug happens because X"
- "Likely cause is Y"
- "Related to feature Z"

### Step 4: Test Hypotheses
- Add logging at key points
- Use debugger breakpoints
- Modify inputs to test assumptions
- Check edge cases

### Step 5: Verify Fix
- Reproduce original issue (should fail)
- Apply fix
- Reproduce again (should succeed)
- Run full test suite

## Debugging Tools

### Node.js Debugger
```bash
# Start with debugger
node --inspect app.js

# Chrome: chrome://inspect
```

### Console Logging
```javascript
console.log('Value:', value);
console.error('Error:', error);
console.table(data);
console.time('operation');
```

### Network Inspector
```bash
# Curl request
curl -v https://api.example.com/endpoint

# Detailed headers
curl -vv https://api.example.com/endpoint
```

### Database Query Logging
```sql
-- PostgreSQL
SET log_statement = 'all';
SELECT * FROM pg_stat_statements;
```

## Common Issues & Fixes

### N+1 Query Problem
**Problem:** Loop makes database query per item
```javascript
// BAD: N+1 queries
users.forEach(user => {
  const posts = db.query('SELECT * FROM posts WHERE user_id = ?', user.id);
});

// GOOD: Single JOIN query
const result = db.query('SELECT u.*, p.* FROM users u LEFT JOIN posts p...');
```

### Memory Leak
**Problem:** Objects not garbage collected
```javascript
// Bad: Reference not released
const cache = {};
function addToCache(key, value) {
  cache[key] = value; // Grows forever
}

// Good: Clear old entries
function addToCache(key, value, ttl = 3600) {
  cache[key] = value;
  setTimeout(() => delete cache[key], ttl * 1000);
}
```

### Race Condition
**Problem:** Async operations order unpredictable
```javascript
// Bad: No ordering
async function updateUser(id, data) {
  await db.update(id, data);
  await sendEmail(id);
}

// Good: Proper sequencing
async function updateUser(id, data) {
  await db.update(id, data);
  const user = await db.get(id);
  await sendEmail(user.email);
}
```
