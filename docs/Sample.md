# Sample Works

## Technical Doc: [Sample PDF](https://darsanaks.github.io/DarsanaKS/TechCodeSampleDoc.pdf)

## User Manual: [Sample PDF](https://darsanaks.github.io/DarsanaKS/Sample%20User%20Manual%201.pdf)

## API Documentation

### [Sample PDF](https://darsanaks.github.io/DarsanaKS/TW%20API%20Doc.pdf)

### Sample Product Inventory API Documentation

This document describes the endpoints for the Product Inventory API, allowing users to view, search, and manage product records. All endpoints require authentication and are accessible via the base URL: `https://api.yourcompany.com/v1`.

#### Get All Products

##### Description

Retrieves a paginated list of all active product records in the system. Optional query parameters (category in this sample) can be used to filter the results.


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


##### Status

Satus: 200 OK (Success)

##### Response Body

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
      "name": "Standard Widget1",
      "price": 19.99,
      "stock_count": 50,
      "is_active": true
    }
    {
      "product_id": "PRD-4522",
      "name": "Standard Widget2",
      "price": 19.99,
      "stock_count": 50,
      "is_active": true
    }
  ]
}
```

**Additonal Info**: <br>

The terms total, limit, offset, and data are standard conventions used, specifically for handling pagination.<br>
The pagination fields - total, limit, offset, data - are used to manage a large dataset that is too big to return in a single response (e.g., if you have 10,000 products).

**Total**: This is the total number of all available records in the entire database that match the query, not just the ones returned in the current response.<br>
**Category**: The category parameter comes from the imaginary requirements of the Product Inventory Service.<br>
**Data**: This is the primary key that holds the actual list of product objects (the items being requested).





