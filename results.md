# VERIFIABLE RESULTS FROM ECOMMERCE DATA ANALYTICS PIPELINE ORCHESTRATION

### DOCKERIZED IMPLEMENTATION SETUP (AIRFLOW, AIRBYTE, POSTGRES)
![docker_containers](images\docker_containers.png)

### DB comformation of data on source DB `pipeline_source` after seeding
![seed_conformation](images\seed_conformation.png.png)

### Airbyte Connection from source `pipeline_source` to destination `pipeline_warehouse`.
![airbyte_connection](images\airbyte_connection.png)

### Orchestrated Airflow connection to Airbyte for incremental data sync (cursor)
![airflow_to_airbyte_conn](images\airflow_to_airbyte_conn.png)

### Successful Orchestration of data sync from `pipeline_source` to `pipeline_warehouse` and `dbt models run`
![airflow_dags_run](images\airflow_dags_run.png)

### Conformation of data on destination `pipeline_warehouse` via successful orchestration
![conformation_destination](images\conformation_destination.png)

 **Executing Analytic psql query on destination warehouse**
 ![analytic_query](images\analytic_query.png)

### Injecting new data (seed_incremental.py) to validate auto incremental fresh via airflow DAG workflow
![seed_incremental_injection](images\seed_incremental_injection.png)

### Orchestrated Airflow's DAG workflow succeeded after incremental seed injection.
![DAG_workflow_success_after_injection](images\DAG_workflow_success_after_injection.png) 


### Warehouse state after successful workflow execution
![pipeline_warehouse_after_injection_and_workflowrun](images\pipeline_warehouse_after_injection_and_workflowrun.png)

 **Executing Analytic psql query on destination warehouse after incremental seeding**
 ![analytical_query_after_injection](images\analytical_query_after_injection.png)


 ## END OF RESULT. THANKS FOR FOLLOWING. SEE README TO FULL DOCUMENTATION ON PROJECT