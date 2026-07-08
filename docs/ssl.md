# SSL Setup Strategy

## Current Deployment

The application is currently deployed using HTTP because no public domain is configured.

---

## Production HTTPS Strategy

In production, HTTPS would be enabled using:

- NGINX
- Let's Encrypt
- Certbot

Installation:

```bash
sudo apt install certbot python3-certbot-nginx
```

Generate Certificate

```bash
sudo certbot --nginx
```

Automatic Renewal

```bash
sudo certbot renew --dry-run
```

---

## Benefits

- Secure communication
- Data encryption
- Browser trust
- Automatic renewal