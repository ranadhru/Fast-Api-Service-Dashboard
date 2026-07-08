#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

docker exec postgres-db pg_dump \
-U postgres ai_service_db \
> backup_$DATE.sql