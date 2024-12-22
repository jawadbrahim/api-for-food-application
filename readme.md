Food Application



This is a RESTful API for managing food-related operations, including authentication, authorization, and CRUD functionalities. The application is built using Python, Flask, Flask-RESTful, PostgreSQL, Redis, and other modern tools for building scalable and secure APIs.

Features

Authentication and Authorization

Secure User Authentication: Users authenticate using JWT tokens to access protected endpoints.

Role-based Authorization: Users with different roles (e.g., admin, regular user) can perform different actions on the application (e.g., admins can create and delete food items, regular users can only view food items).
CRUD Operations

Create: Add new food items to the system with details like name, description, price, etc.
Read: Retrieve food item details.
Update: Modify the details of an existing food item.
Delete: Remove a food item from the system.
Rate Limiting

Prevent abuse by limiting the number of requests a user can make in a given period (e.g., 100 requests per hour).
Schema Validation

Enforced Data Integrity: Ensure that all incoming data for food items and user operations follows a defined structure using Pydantic models.

Modular Architecture

Blueprints: The application is structured into blueprints to separate concerns, making it easy to maintain and scale.
Service Factories: Services are organized into factories to facilitate testing and future expansions.

Password Hashing
bcrypt: User passwords are hashed and salted using bcrypt before storage to prevent unauthorized access.

Food Reviews

User Reviews: Users can leave reviews for food items, including likes/dislikes, ratings, and comments.

Caching

Redis Caching: Database query results are cached in Redis to improve performance and reduce load on the PostgreSQL database.
Rate-Limiting Caching: Redis is used for rate-limiting to track the number of requests made by a user.
Search Functionality
Search Food Items: Users can search for food items by name, category, or ingredients.
