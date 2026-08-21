# VERIFIABLE RESULTS FROM ECOMMERCE DATA ANALYTICS PIPELINE ORCHESTRATION

### DOCKERIZED IMPLEMENTATION SETUP (AIRFLOW, AIRBYTE, POSTGRES)
![docker_containers](\ecommerce_dbt\images\image-3.png)

### DB comformation of data on source DB `pipeline_source` after seeding
![seed_conformation](\ecommerce_dbt\images\image-1.png.png)

### Airbyte Connection from source `pipeline_source` to destination `pipeline_warehouse`.
![airbyte_connection](\ecommerce_dbt\images\image-2.png)

### Orchestrated Airflow connection to Airbyte for incremental data sync (cursor)
![airflow_to_airbyte_conn](\ecommerce_dbt\images\image-4.png)

### Successful Orchestration of data sync from `pipeline_source` to `pipeline_warehouse` and `dbt models run`
![airflow_dags_run](\ecommerce_dbt\images\image-5.png)

### Conformation of data on destination `pipeline_warehouse` via successful orchestration
![conformation_destination](\ecommerce_dbt\images\image-6.png)

 **Executing Analytic psql query on destination warehouse**
 ![analytic_query](\ecommerce_dbt\images\image-7.png)

### Injecting new data (seed_incremental.py) to validate auto incremental fresh via airflow DAG workflow
![seed_incremental_injection](\ecommerce_dbt\images\image-8.png)

### Orchestrated Airflow's DAG workflow succeeded after incremental seed injection.
![DAG_workflow_success_after injection](\ecommerce_dbt\images\image-9.png) 


### Warehouse state after successful workflow execution
![pipeline_warehouse_after_injection_and_workflowrun](\ecommerce_dbt\images\image-10.png)

 **Executing Analytic psql query on destination warehouse after incremental seeding**
 ![analytical_query_after_injection](\ecommerce_dbt\images\image-11.png)


 ## END OF RESULT. THANKS FOR FOLLOWING. SEE README TO FULL DOCUMENTATION ON PROJECT