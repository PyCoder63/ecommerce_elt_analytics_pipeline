SELECT
    order_id, customer_id,
    order_date::DATE AS order_date, 
    status
FROM {{ source('pipeline_warehouse', 'orders') }}
WHERE status <> 'cancelled'