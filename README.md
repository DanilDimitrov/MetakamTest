API Documentation
Overview
This API provides access to the Brand and Manufacturer models in the application. It allows you to perform CRUD (Create, Read, Update, Delete) operations on both Brands and Manufacturers.

Base URL
http://<your-domain>/api/v1/
Brands
Get All Brands
Endpoint:

GET /brands
Response:

json
[
    {
        "id": 1,
        "name": "Brand Name",
        "logo": "http://example.com/logo.png",
        "description": "Brand description.",
        "manufacturers": [
            {
                "id": 1,
                "name": "Manufacturer Name"
            }
        ]
    }
]
Get a Brand by ID
Endpoint:

GET /brands/<id>
Parameters:

id: The ID of the brand.
Response:

json
{
    "id": 1,
    "name": "Brand Name",
    "logo": "http://example.com/logo.png",
    "description": "Brand description.",
    "manufacturers": [
        {
            "id": 1,
            "name": "Manufacturer Name"
        }
    ]
}
Create a Brand
Endpoint:

POST /brands
Request Body:

json
{
    "name": "New Brand",
    "logo": "http://example.com/logo_new.png",
    "description": "Description for New Brand",
    "manufacturers": [1, 2]  // List of manufacturer IDs to associate with the brand
}
Response:

json
{
    "id": 2,
    "name": "New Brand",
    "logo": "http://example.com/logo_new.png",
    "description": "Description for New Brand",
    "manufacturers": [
        {
            "id": 1,
            "name": "Manufacturer Name"
        },
        {
            "id": 2,
            "name": "Another Manufacturer"
        }
    ]
}
Update a Brand
Endpoint:

PUT /brands/<id>
Parameters:

id: The ID of the brand.
Request Body:

json
{
    "name": "Updated Brand",
    "logo": "http://example.com/logo_updated.png",
    "description": "Updated description.",
    "manufacturers": [2, 3]  // Updated list of manufacturer IDs
}
Response:

json
{
    "id": 1,
    "name": "Updated Brand",
    "logo": "http://example.com/logo_updated.png",
    "description": "Updated description.",
    "manufacturers": [
        {
            "id": 2,
            "name": "Updated Manufacturer"
        },
        {
            "id": 3,
            "name": "Another Manufacturer"
        }
    ]
}
Manufacturers
Get All Manufacturers
Endpoint:

GET /manufacturers
Response:

json
[
    {
        "id": 1,
        "name": "Manufacturer Name",
        "description": "Manufacturer description."
    }
]
Get a Manufacturer by ID
Endpoint:

GET /manufacturers/<id>
Parameters:

id: The ID of the manufacturer.
Response:

json
{
    "id": 1,
    "name": "Manufacturer Name",
    "description": "Manufacturer description."
}
Create a Manufacturer
Endpoint:

POST /manufacturers
Request Body:

json
{
    "name": "New Manufacturer",
    "description": "Description for New Manufacturer"
}
Response:

json
{
    "message": "Manufacturer added successfully!"
}
Error Handling
Responses will include HTTP status codes to indicate the outcome of the request:

200 OK: Request was successful.
201 Created: Resource was created successfully.
400 Bad Request: Invalid request, often due to missing or incorrect parameters.
404 Not Found: Resource not found.
500 Internal Server Error: An unexpected error occurred on the server.
Notes
All requests should be made with appropriate headers, such as Content-Type: application/json.
Ensure that you have valid data when creating or updating resources to avoid validation errors.
