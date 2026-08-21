from airflow import DAG
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='ecommerce_elt_pipeline',
    start_date=datetime(2026, 8, 15),
    schedule='0 */6 * * *',  # Runs every 6 hours: 00:00, 06:00, 12:00, 18:00
    catchup=False,
    max_active_runs=1,       # Prevents overlapping runs if a sync takes too long
    default_args=default_args,
) as dag:

    trigger_airbyte = AirbyteTriggerSyncOperator(
        task_id='trigger_airbyte_sync',
        airbyte_conn_id='airbyte_default',
        connection_id='dcc9c659-ced8-4583-8fa0-401ec672036b',
        asynchronous=False,
    )

    run_dbt_models = BashOperator(
        task_id='run_dbt_transformations',
        bash_command='cd /opt/airflow/dbt/ecommerce_dbt && dbt run',
    )

    trigger_airbyte >> run_dbt_models