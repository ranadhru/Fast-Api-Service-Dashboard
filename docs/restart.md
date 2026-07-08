# Restart Strategy

Docker Compose uses:

```yaml
restart: always
```

This ensures containers automatically restart after:

- Container Crash
- Docker Restart
- EC2 Reboot

---

## Health Checks

Each service includes health checks.

Docker automatically detects unhealthy containers.

---

## Failure Recovery

If a service fails:

1. Docker restarts the container.
2. Health checks verify availability.
3. NGINX resumes serving requests.

---

## Future Improvements

- Rolling Deployments
- Blue/Green Deployment
- Kubernetes Self-Healing