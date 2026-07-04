# Database Migration Best Practices

## Migration Strategy

### Naming Convention
```
001_create_users_table.sql
002_add_email_index.sql
003_create_posts_table.sql
004_rename_user_id_column.sql
```

### Safe Migration Pattern
```sql
-- UP: Add new column with default
ALTER TABLE users ADD COLUMN status VARCHAR(50) DEFAULT 'active';

-- DOWN: Remove column
ALTER TABLE users DROP COLUMN status;
```

## Zero-Downtime Deployments

### Add Column (Safe)
```sql
-- Step 1: Add column with default (no downtime)
ALTER TABLE users ADD COLUMN new_field VARCHAR(255) DEFAULT 'value';

-- Step 2: Backfill data (can be slow)
UPDATE users SET new_field = old_field WHERE new_field IS NULL;

-- Step 3: Add NOT NULL constraint (after app updated)
ALTER TABLE users ALTER COLUMN new_field SET NOT NULL;
```

### Drop Column (Safe)
```sql
-- Step 1: Make column nullable
ALTER TABLE users ALTER COLUMN old_field DROP NOT NULL;

-- Step 2: Remove from app code

-- Step 3: Drop column in follow-up migration
ALTER TABLE users DROP COLUMN old_field;
```

### Rename Column (Safe)
```sql
-- Step 1: Create new column
ALTER TABLE users ADD COLUMN user_name VARCHAR(255);

-- Step 2: Copy data
UPDATE users SET user_name = username;

-- Step 3: Remove old code references

-- Step 4: Drop old column
ALTER TABLE users DROP COLUMN username;
```

## Backwards Compatibility

- New code must work with old schema
- Old code must work with new schema
- Never break contract between versions

## Migration Rollback

```bash
# Check status
npm run db:migrate:status

# Rollback one step
npm run db:migrate:down

# Rollback all
npm run db:migrate:down:all
```

## Testing Migrations

```bash
# Test up
npm run db:migrate:up

# Verify data
npm run db:verify

# Test down
npm run db:migrate:down

# Verify restoration
npm run db:verify
```
