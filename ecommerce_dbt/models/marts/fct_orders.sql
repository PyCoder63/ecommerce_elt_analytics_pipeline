{{ 
    config(
        materialized='table'
        ) 
}}
SELECT
    o.order_id, 
    o.customer_id, 
    o.order_date,
    COUNT(oi.order_item_id) AS item_count, 
    SUM(oi.quantity) AS total_quantity, 
    SUM(oi.line_total) AS order_total
FROM {{ ref('stg_orders') }} o
JOIN {{ ref('stg_order_items') }} oi USING (order_id)
GROUP BY o.order_id, o.customer_id, o.order_date