# Telegram Gateway Setup — Pitfalls & Solutions

Session-tested on Termux/Android, 2026-06-27.

## Pitfall 1: `hermes config set` writes YAML strings, not lists

**Symptom**: Gateway log shows "No user allowlists configured" even after setting `telegram.allowed_users`.

**Root cause**: `hermes config set telegram.allowed_users "1703267346"` writes the value as a YAML string `'[1703267346]'` instead of a list `[1703267346]`. The gateway's allowlist parser doesn't recognize string-format lists.

**Fix**: Edit config.yaml directly:
```bash
sed -i "s/allowed_users: '\[1703267346\]'/allowed_users: [1703267346]/" ~/.hermes/config.yaml
```

Or use `nano ~/.hermes/config.yaml` and manually remove the quotes around the list.

## Pitfall 2: Token must be in TWO sections

**Symptom**: "No messaging platforms enabled" even with token set.

**Root cause**: Hermes reads token from both `platforms.telegram.token` AND `telegram.token`. Setting only one is insufficient.

**Fix**:
```bash
hermes config set platforms.telegram.token "YOUR_TOKEN"
hermes config set telegram.token "YOUR_TOKEN"
```

## Pitfall 3: Stale gateway processes

**Symptom**: Config changes don't take effect, logs show old state.

**Root cause**: Multiple gateway processes running; new one may not start if old one holds the log file lock.

**Fix**:
```bash
pkill -f "hermes gateway" 2>/dev/null; sleep 3
# Verify clean:
ps aux | grep "gateway run" | grep -v grep  # should be empty
# Then start fresh:
hermes gateway run > /tmp/gw.log 2>&1 &
```

## Pitfall 4: `display.platforms.telegram.token` section

**Symptom**: Token appears correct but gateway still ignores it.

**Root cause**: There's a third token location under `display.platforms.telegram.token` (for UI display). If this has a stale/wrong token, it can confuse debugging.

**Fix**: Clear it if not needed:
```bash
hermes config set display.platforms.telegram.token ""
```

## Pitfall 5: `platforms.telegram.enabled: true` is REQUIRED

**Symptom**: "No messaging platforms enabled" in gateway log despite token being set in both sections, plugin enabled, and python-telegram-bot installed.

**Root cause**: `GatewayConfig.get_connected_platforms()` checks `config.enabled` first (line 560 of `gateway/config.py`). `PlatformConfig.enabled` defaults to `False`. Without `enabled: true` in `platforms.telegram`, the platform is skipped even with a valid token.

**Fix**:
```bash
hermes config set platforms.telegram.enabled true
```

Then restart gateway:
```bash
pkill -f "hermes gateway" 2>/dev/null; sleep 3
hermes gateway run > /tmp/gw.log 2>&1 &
```

**Debugging note**: If you've verified token (both sections), plugin enabled, dependency installed, stale processes killed, and `allowed_users` is correct format — but STILL see "No messaging platforms enabled" — this is the missing piece. The gateway requires BOTH `enabled: true` AND a token to consider a platform connected.

## Pitfall 6: Discord lazy-install blocks Telegram gateway startup

**Symptom**: `hermes gateway status` shows gateway running, but gateway.log stops at "Starting Hermes Gateway..." / "skipping session suspension" with NO "Connecting to telegram..." line even after 5+ minutes.

**Root cause**: On first run (or after venv cleanup), the gateway lazy-installs Python dependencies for ALL detected platform adapters — including `discord.py[voice]==2.7.1` and `brotlicffi==1.2.0.1` even if the user only needs Telegram. On Termux, this pip install is extremely slow (2-5+ minutes) and runs **sequentially before any platform connects**. Telegram waits until all platform deps finish installing.

**How to detect**:
```bash
ps -ef | grep gateway | grep -v grep
# Child process running: "pip install discord.py[voice]..." → this is the blocker
```

Also visible in agent.log:
```
INFO tools.lazy_deps: Lazy-installing discord.py[voice]==2.7.1 brotlicffi==1.2.0.1 for feature 'platform.discord'
```

**Fix — option 1: Pre-install Discord deps (one-time cost)**:
```bash
~/.hermes/hermes-agent/venv/bin/pip install "discord.py[voice]==2.7.1" brotlicffi
```

**Fix — option 2: Disable Discord in config (skip install entirely)**:
```bash
hermes config set platforms.discord.enabled false
```
Or remove the `discord:` section from `platforms:` in config.yaml entirely.

After either fix, restart gateway:
```bash
pkill -f "hermes gateway" 2>/dev/null; sleep 3
hermes gateway run > /tmp/gw.log 2>&1 &
```

**Key insight**: The gateway does NOT parallelize platform dep installation. All platforms wait for all deps. On resource-constrained devices (Termux/Android), pre-installing or disabling unused platforms is the fastest path to getting Telegram connected.

## Verification checklist

After setup, run:
```bash
sleep 8
grep -i "telegram\|platform\|enabled" /tmp/gw.log
```

Expected: NO "No messaging platforms enabled" line.
Expected: NO "No user allowlists configured" line.
Expected: YES "✓ telegram connected" line.

If either "No messaging platforms" or "No user allowlists" appears, re-check pitfalls 1-5 above.
If Telegram still doesn't connect after 2+ minutes with no log movement, check pitfall 6 (lazy-install blocking).
