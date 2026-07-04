# Observability Setup Checklist

## Metrics to Track

### Business Metrics
- Active users (DAU, MAU)
- Conversion rate (signup, payment)
- Revenue
- Customer churn
- NPS (Net Promoter Score)

### Technical Metrics
- Request rate (req/sec)
- Error rate (5xx, 4xx per endpoint)
- Latency (p50, p95, p99)
- Throughput (req/sec capacity)
- Uptime (9s: 99.9%, 99.99%)

### Infrastructure Metrics
- CPU usage
- Memory usage
- Disk usage
- Network I/O
- Database connections

## Logging Strategy

### Structured Logging Format
```json
{
  "timestamp": "2026-07-04T16:47:00Z",
  "level": "ERROR",
  "service": "checkout",
  "trace_id": "abc-123-def",
  "user_id": "user-456",
  "message": "Payment processing failed",
  "error": "gateway_timeout",
  "duration_ms": 5000,
  "tags": ["payment", "critical"]
}
```

### Log Levels
- ERROR: Actionable errors (auth failed, db connection lost)
- WARN: Suspicious but not critical (retry needed, rate limit approaching)
- INFO: Important events (user login, payment completed)
- DEBUG: Detailed info for troubleshooting (query executed, cache hit)

### What NOT to Log
- Passwords, API keys, tokens
- Credit card numbers
- PII (email, phone, SSN)
- Debug dumps (dump entire object)

## Alerting Rules

### Error Rate Alert
- Threshold: > 5% error rate
- Window: 5 min average
- Action: Page on-call

### Latency Alert
- Threshold: p99 > 500ms (adjust per endpoint)
- Window: 5 min average
- Action: Create ticket

### Database Alert
- Threshold: Connection pool > 90% full
- Window: 1 min average
- Action: Notify infra team

### Disk Space Alert
- Threshold: > 80% used
- Window: Immediate
- Action: Page on-call

## Dashboard Examples

### Service Health Dashboard
- Error rate (red if > 5%)
- Latency p99 (yellow if > 2x baseline)
- Uptime %
- Recent incidents

### Team Dashboard
- Deployments (timeline)
- Incident count
- Average resolution time
- On-call rotation
