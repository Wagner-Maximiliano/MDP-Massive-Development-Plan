# Error Handling and Observability Protocol

MDP-managed work must make failures easy to identify, understand, and recover from.

## Core rule

Any task, script, module, function, automation, or agent workflow that can fail should include appropriate error handling and useful diagnostics.

Failures should not disappear silently. They should leave enough evidence to understand what failed, where it failed, why it likely failed, and what should happen next.

## Required practices

When building or modifying code, automation, scripts, cron jobs, or workflow modules:

1. Catch expected errors at the right boundary.
2. Preserve the original error message and stack trace where useful.
3. Add context to errors, such as operation, path, task ID, provider, request type, or external service.
4. Avoid broad silent catches.
5. Fail fast when continuing would corrupt state or hide the problem.
6. Retry only when the failure is likely transient.
7. Use bounded retries with backoff for network, provider, rate-limit, and temporary service errors.
8. Log important state transitions and failure points.
9. Return structured failure information when a script or tool is consumed by another agent.
10. Include recovery or escalation guidance when possible.

## Bad patterns

Avoid:

- catching every exception and continuing without logging
- replacing the real error with a vague message
- retrying forever
- swallowing provider/auth/token errors
- creating partial output without marking it partial
- hiding failed verification
- reporting success when warnings or skipped steps matter

## Minimum error report shape

Use this shape when reporting or logging a meaningful failure:

- operation:
- component:
- input or target:
- error type:
- error message:
- stack trace or source location, if available:
- likely cause:
- retry attempted:
- current state:
- recommended next action:
- whether Human Owner input is required:

## Relationship to debugging

Error handling supports systematic debugging. When an error happens, agents should use root-cause investigation before random fixes.

## Relationship to project health

Project health monitors should watch for repeated errors, silent failures, auth expiry, provider failures, token exhaustion, stale tasks, and missing outputs.
