# Project Health Monitoring Protocol

The Human Owner is not the monitoring system.

MDP-managed projects should detect hiccups proactively through agent-declared and system-detected signals.

## Agent-declared signals

- task state
- owner role
- heartbeat
- blocker reason
- confidence score
- last verification result
- next action
- whether Human Owner input is required

## System-detected signals

- new blocked task not acknowledged
- no ready tasks while project is live
- all tasks done while project is still live
- no activity for a threshold
- repeated worker failures
- provider or API errors
- token exhaustion
- authentication expiry
- unhandled exceptions or repeated handled exceptions
- scripts or workers that exit without structured status
- stale claims or silent workers

## Project states

- live
- waiting
- paused
- completed
- archived

When the project is intentionally waiting, monitoring should not spam the PA. When live work stalls unexpectedly, notify the PA with compact evidence.
