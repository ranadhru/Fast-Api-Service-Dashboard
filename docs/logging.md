# Logging Strategy

## Application Logs

FastAPI uses Python's built-in logging module to record application events.

Logs include:

- API Requests
- Health Checks
- Errors
- Startup Events

---

## Docker Logs

Container logs are available using:

```bash
docker logs ai-dashboard
```

---

## NGINX Logs

NGINX maintains:

- Access Logs
- Error Logs

---

## PostgreSQL Logs

Database logs are available through the PostgreSQL container.

---

## Redis Logs

Redis logs are available through the Redis container.

---

## Future Improvements

- Centralized Logging
- ELK Stack
- Grafana Loki