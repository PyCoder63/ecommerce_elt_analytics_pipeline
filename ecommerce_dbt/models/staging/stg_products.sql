SELECT
    product_id,
    name AS product_name,
    category, 
    unit_price
FROM {{ source('pipeline_warehouse', 'products') }}