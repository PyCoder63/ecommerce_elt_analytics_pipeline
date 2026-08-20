SELECT
    order_item_id, 
    order_id, 
    product_id, 
    quantity, 
    line_total
FROM {{ source('pipeline_warehouse', 'order_items') }}