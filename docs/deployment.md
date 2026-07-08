# Deployment Guide

## Overview

This project is deployed on an AWS EC2 Ubuntu instance using Docker Compose.

The deployment process is fully automated through GitHub Actions. Every push to the `main` branch triggers the CI/CD pipeline, which builds a new Docker image, pushes it to Docker Hub, and deploys the latest version to the EC2 server.

---

## Deployment Architecture

Developer

↓

GitHub Repository

↓

GitHub Actions

↓

Docker Hub

↓

AWS EC2

↓

Docker Compose

↓

NGINX

↓

FastAPI

↓

PostgreSQL + Redis

---

## Prerequisites

- AWS EC2 Ubuntu Server
- Docker
- Docker Compose
- Git
- Docker Hub Account
- GitHub Repository
- SSH Key Pair

---

## Deployment Steps

### Clone Repository

```bash
git clone https://github.com/<username>/Fast-Api-Service-Dashboard.git

cd Fast-Api-Service-Dashboard
```

### Configure Environment Variables

Create a `.env` file.

Example:

```env
POSTGRES_DB=ai_service_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres-db
POSTGRES_PORT=5432

REDIS_HOST=redis-cache
REDIS_PORT=6379
```

### Start Containers

```bash
docker compose up -d
```

### Verify

```bash
docker ps
```

Open:

```
http://<EC2-PUBLIC-IP>
```

Swagger:

```
http://<EC2-PUBLIC-IP>/docs
```

---

## Continuous Deployment

Every push to the main branch automatically:

- Builds Docker Image
- Pushes Image to Docker Hub
- Connects to EC2
- Pulls Latest Image
- Restarts Docker Compose

No manual deployment is required.

---

## Health Check

Application Health Endpoint:

```
/health
```