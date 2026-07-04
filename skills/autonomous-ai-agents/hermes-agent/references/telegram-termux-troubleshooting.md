# Telegram on Termux — Setup & Troubleshooting

## Why This Page Exists

The official `telegram-gateway-quick.md` says: set token + restart. That is **not enough** on Termux/Android. This page covers the full setup, the config structure pitfalls, and the "No messaging platforms enabled" loop that happens when dependencies are missing or stale gateway processes hold locks.

## Prerequisites

- Hermes Agent installed on Termux
- A Telegram bot token from @BotFather (format: `123456789:ABCdef...`)
- `python-telegram-bot` installed in the Hermes venv

## Full Setup (do this in order)

### Step 1: Install the dependency

```bash
pip3 install python-telegram-bot
```

Verify:
```bash
python3 -c "import telegram; print(telegram.__version__)"
```

### Step 2: Set the token in BOTH config sections

Hermes config.yaml has **two** `telegram:` sections. Both need the token:

```bash
# The platform adapter section (used by telegram-platform plugin)
hermes config set platforms.telegram.token "YOUR_TOKEN_HERE"

# The standalone section (used by gateway's internal adapter)
hermes config set telegram.token "YOUR_TOKEN_HERE"
```

### Step 3: Enable the plugin

```bash
hermes plugins enable telegram-platform
```

### Step 4: Set gateway-related flags

```bash
hermes config set gateway.enabled true
hermes config set gateway.streaming.enabled true
hermes config set web.use_gateway true
hermes config set tts.use_gateway true
hermes config set image_gen.use_gateway true
```

### Step 5: Kill any stale gateway processes

```bash
pkill -f "hermes gateway" 2>/dev/null; sleep 2
```

### Step 6: Start gateway

```bash
hermes gateway run > /tmp/gw.log 2>&1 &
```

### Step 7: Verify

```bash
sleep 5
hermes gateway status
# Should show: ✓ Gateway is running
```

Check log for platform detection:
```bash
grep -i "telegram\|platform\|enabled" /tmp/gw.log
```

You should NOT see "No messaging platforms enabled". If you do, see troubleshooting below.

### Step 8: Test the bot

Open Telegram → find your bot → send "test"

## Common Issues

### "No messaging platforms enabled" in gateway log

**Root cause**: Gateway started before `python-telegram-bot` was installed, or platform adapter failed to import.

**Fix**:
1. Kill all gateway processes: `pkill -f "hermes gateway" 2>/dev/null`
2. Verify dependency: `python3 -c "import telegram; print('OK')"`
3. Re-enable plugin: `hermes plugins enable telegram-platform`
4. Restart gateway: `hermes gateway run > /tmp/gw.log 2>&1 &`
5. Wait 5-8 seconds before checking logs (Python import takes time)

### Multiple gateway processes holding log file

**Symptom**: Gateway status shows multiple PIDs, logs are empty or stale.

**Fix**:
```bash
pkill -9 -f "hermes gateway" 2>/dev/null
sleep 3
# Verify clean:
ps aux | grep "gateway run" | grep -v grep
# Should be empty. Then start fresh:
hermes gateway run > /tmp/gw.log 2>&1 &
```

### Token in wrong section

**Symptom**: Token set but gateway still ignores Telegram.

**Diagnosis**: Check both sections:
```bash
grep -n "token" ~/.hermes/config.yaml | grep -i "telegram\|8568632248"
```

You should see TWO lines — one under `platforms.telegram` and one under `telegram:`.

### Gateway dies when Termux is backgrounded

**Symptom**: Bot stops responding when you switch apps.

**Fix**: This is expected on Android. The gateway process is killed by Android battery optimization. Options:
- Keep Termux in foreground with screen lock
- Use `termux-wake-lock` (if available)
- Accept that the gateway only runs while Termux is open

### `hermes config set` writes to wrong section

**Symptom**: `hermes config set platforms.telegram.token X` creates a new section instead of updating existing.

**Diagnosis**: Check if token appears in both sections:
```bash
grep -c "token.*YOUR_TOKEN" ~/.hermes/config.yaml
```

If only in `platforms.telegram` but not in `telegram:`, add it manually:
```bash
hermes config set telegram.token "YOUR_TOKEN_HERE"
```

## Config Structure Reference

```
~/.hermes/config.yaml
├── platforms:
│   └── telegram:           ← Used by telegram-platform plugin
│       token: "..."
├── telegram:               ← Used by gateway's internal adapter
│   token: "..."
│   reactions: false
│   channel_prompts: {}
│   allowed_chats: ''
│   extra:
│     rich_messages: true
├── gateway:
│   enabled: true
│   streaming:
│     enabled: true
├── plugins:
│   enabled:
│     - platforms/telegram
├── web:
│   use_gateway: true
├── tts:
│   use_gateway: true
└── image_gen:
    use_gateway: true
```

## Verification Checklist

- [ ] `python3 -c "import telegram"` succeeds
- [ ] Token in `platforms.telegram.token`
- [ ] Token in `telegram.token`
- [ ] `plugins.enabled` contains `platforms/telegram`
- [ ] `gateway.enabled: true`
- [ ] `gateway.streaming.enabled: true`
- [ ] `web.use_gateway: true`
- [ ] No stale gateway processes (`ps aux | grep gateway`)
- [ ] Gateway log does NOT contain "No messaging platforms enabled"
- [ ] Bot responds to messages in Telegram DM
