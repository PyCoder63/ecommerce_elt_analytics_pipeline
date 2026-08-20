SELECT
    customer_id,
    name AS customer_name, 
    LOWER(email) AS email, 
    signup_date,
    country
FROM {{ source('pipeline_warehouse', 'customers') }}