CREATE USER airbyte_user WITH PASSWORD 'admin';

CREATE DATABASE pipeline_source;
CREATE DATABASE pipeline_warehouse;

GRANT ALL PRIVILEGES ON DATABASE pipeline_source TO airbyte_user;
GRANT ALL PRIVILEGES ON DATABASE pipeline_warehouse TO airbyte_user;