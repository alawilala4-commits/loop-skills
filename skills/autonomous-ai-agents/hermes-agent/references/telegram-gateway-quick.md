# Telegram Gateway Quick Reference

## Setup (5 minutes)

### 1. Create Bot
```
Telegram → @BotFather → /newbot → name → username → get token
```

### 2. Configure Hermes
Edit `~/.hermes/config.yaml`:
```yaml
platforms:
  telegram:
    streaming: true
    token: "YOUR_BOT_TOKEN_HERE"
```

### 3. Enable Gateway
```bash
hermes gateway restart
```

### 4. Test
Open Telegram → find your bot → send "test"

## Common Issues

| Problem | Fix |
|---------|-----|
| Bot not responding | Check token in config.yaml |
| Gateway crash | `hermes gateway status` → check logs |
| Bot only works in DMs | Normal — Telegram bots need start/command in DM |
| Media not sending | Ensure `media_delivery_allow_dirs` configured |

## Telegram-Specific Features
- **Inline buttons**: Not supported natively
- **Voice messages**: Auto-transcribed via STT
- **Images**: Downloaded and processed via vision tool
- **File sharing**: Supported, saved to temp dir
- **Rich messages**: Configurable via `platforms.telegram.rich_messages`

## Gateway Commands (in Telegram chat)
```
/restart  - Restart gateway
/status   - Show platform status
/approve   - Approve pending command
/deny     - Deny pending command
```
