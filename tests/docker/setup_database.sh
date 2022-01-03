#!/bin/bash

while ! nc -z "${DB_HOST:-127.0.0.1}" "${DB_PORT:-3306}"; do
  echo "Waiting for database connection..."
  sleep 1
done

echo "Database is up"

echo "Creating database ${DB_NAME:-phpipam}"
docker exec -ti docker_phpipam_1 sh -c 'mysql -h database -u phpipam -pphpipamadmin phpipam < /phpipam/db/SCHEMA.sql'

echo "Activating API"
mysql -u phpipam -pphpipamadmin -h "${DB_HOST:-127.0.0.1}" phpipam --execute="UPDATE settings SET api=1 WHERE id=1;"

echo "Inserting API application"
mysql -u phpipam -pphpipamadmin -h "${DB_HOST:-127.0.0.1}" phpipam --execute="INSERT INTO api (app_id, app_code, app_permissions, app_security, app_lock_wait) VALUES ('ansible','aAbBcCdDeEfF00112233445566778899',2,'ssl_token',0);"
