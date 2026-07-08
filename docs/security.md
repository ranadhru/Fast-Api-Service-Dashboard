# Security Measures

## Environment Variables

Sensitive configuration is stored in a `.env` file.

The `.env` file is excluded from Git using `.gitignore`.

An `.env.example` file is included for reference.

---

## AWS Security Group

Only the required ports are exposed.

| Port | Purpose |
|------|----------|
|22|SSH|
|80|HTTP|
|443|HTTPS|

---

## SSH Authentication

The server uses SSH Key authentication.

Password authentication is disabled in production.

---

## Docker Security

- Docker containers are isolated.
- Environment variables are injected securely.
- Health checks monitor application availability.
- Containers automatically restart on failure.

---

## Firewall

Ubuntu UFW may be configured as:

```bash
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

---

## Future Improvements

- AWS Secrets Manager
- Docker Secrets
- Fail2Ban
- IAM Roles
- Cloudflare WAF