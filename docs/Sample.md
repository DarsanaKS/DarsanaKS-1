# Sample Works

## Technical Doc: [Sample PDF](https://darsanaks.github.io/DarsanaKS/TechCodeSampleDoc.pdf)

## User Manual: [Sample PDF](https://darsanaks.github.io/DarsanaKS/Sample%20User%20Manual%201.pdf)

## API Documentation: [Sample PDF](https://darsanaks.github.io/DarsanaKS/TW%20API%20Doc.pdf)
### Product Inventory API Documentation

This document describes the endpoints for the Product Inventory API, allowing users to view, search, and manage product records. All endpoints require authentication and are accessible via the base URL: `https://api.yourcompany.com/v1`.

#### Get All Products

Retrieves a paginated list of all active product records in the system. Optional query parameters can be used to filter the results.

##### Base URL
https://api.yourcompany.com/v1

##### Endpoint Details

| Method | Path | Description |
| :--- | :--- | :--- |
| **GET** | `/products` | Retrieves the list of products. |

##### Parameters

| Name | Type | Description | Required | Default |
| :--- | :--- | :--- | :--- | :--- |
| **`limit`** | `integer` | Maximum number of results to return per page. | No | 10 |
| **`offset`** | `integer` | The number of records to skip (used for pagination). | No | 0 |
| **`category`** | `string` | Filters products by their primary category. | No | All |

##### Responses

Satus: 200 OK (Success)

Returns a list of products and pagination metadata.

```
json
{
  "total": 150,
  "limit": 10,
  "offset": 0,
  "data": [
    {
      "product_id": "PRD-4521",
      "name": "Standard Widget",
      "price": 19.99,
      "stock_count": 50,
      "is_active": true
    }
    // ... more products
  ]
}
```