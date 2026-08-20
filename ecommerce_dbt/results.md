# VERIFIABLE RESULTS FROM ECOMMERCE DATA ANALYTICS PIPELINE ORCHESTRATION

### DOCKERIZED IMPLEMENTATION SETUP (AIRFLOW, AIRBYTE, POSTGRES)
![docker_containers](image-3.png)

### DB comformation of data on source DB `pipeline_source` after seeding
![seed_conformation](image-1.png)

### Airbyte Connection from source `pipeline_source` to destination `pipeline_warehouse`.
![airbyte_connection](image-2.png)

### Orchestrated Airflow connection to Airbyte for incremental data sync (cursor)
![alt text](image-4.png)

### Successful Orchestration of data sync from `pipeline_source` to `pipeline_warehouse` and `dbt models run`
![airflow_dags_run](image-5.png)

### Conformation of data on destination `pipeline_warehouse` via successful orchestration
![conformation_destination](image-6.png)

 **Executing Analytic query on destination warehouse**
 ![analytic_query](image-7.png)

### Injecting new data (seed_incremental.py) to validate auto incremental fresh via airflow DAG workflow
![seed_incremental_injection](image-8.png)

