{{ 
    config(
        materialized='table'
        ) 
}}

SELECT
    c.customer_id, 
    c.customer_name, 
    c.email, 
    c.country, 
    c.signup_date,
    COUNT(o.order_id) AS lifetime_orders,
    COALESCE(SUM(oi.line_total),0) AS lifetime_revenue
FROM {{ ref('stg_customers') }} c
LEFT JOIN {{ ref('stg_orders') }} o USING (customer_id)
LEFT JOIN {{ ref('stg_order_items') }} oi USING (order_id)
GROUP BY c.customer_id, c.customer_name, c.email, c.country, c.signup_date