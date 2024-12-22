Food Application API Documentation
Overview
This is a RESTful API designed for managing food-related operations, including user authentication and CRUD functionalities. The application leverages Python, Flask, Flask-RESTful, PostgreSQL, Redis, and other modern technologies to ensure scalability, performance, and security.

Features
Authentication
JWT-based Authentication: Users authenticate via JWT tokens, ensuring secure access to protected endpoints. Tokens are issued upon successful login and are required for accessing restricted operations.
Password Hashing: Passwords are securely hashed and salted using bcrypt before storage, ensuring protection against unauthorized access.
CRUD Operations for Food Items
Create: Add new food items with detailed information, including name, description, price, and other attributes.
Read: Retrieve details of a specific food item by ID.
Update: Modify the details of an existing food item (e.g., update the price, name, or description).
Delete: Remove a food item from the system.
Search: Users can search for food items by title or keyword, with full-text search enabled.
Rate Limiting
Request Limiting: Prevent abuse by limiting the number of requests a user can make within a specified period (e.g., 100 requests per hour).
Redis Rate-Limiting: Redis is used to track and manage the number of requests made by a user.
Schema Validation
Enforced Data Integrity: The system ensures that incoming data adheres to a predefined structure using Pydantic models, guaranteeing consistency and validation of inputs.
Modular Architecture
Blueprints: The application is divided into blueprints to separate concerns, making the codebase easier to manage and extend.
Service Factories: Services are organized into factory functions, improving testability and facilitating future expansions of the API.
Food Reviews
User Reviews: Users can submit reviews for food items. Reviews include ratings (1-5 stars), comments, and like/dislike status.
Caching
Redis Caching: Frequently accessed food items are cached in Redis to reduce the load on the PostgreSQL database and improve response times.
Rate-Limiting Caching: Redis is also used to track the number of requests made by a user, ensuring that the rate limit is respected.


