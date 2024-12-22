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
Order Management (New Feature)
Users can create and manage orders. This includes adding items to the cart, placing orders, and checking the status of previous orders.
Notification System (New Feature)
Email Notifications: Users receive email notifications about their orders, new food items, or promotional discounts.
Technologies Used
Backend: Python, Flask, Flask-RESTful
Database: PostgreSQL
ORM: SQLAlchemy
Caching: Redis (for caching and rate-limiting)
Authentication: JWT-based token authentication
Password Hashing: bcrypt
Validation: Pydantic
Search: Elasticsearch (for advanced search functionality)
Deployment: Environment variables for configurations
Notifications: Email via SMTP (for notifications)
API Endpoints
Authentication
POST /auth/register
Register a new user.

POST /auth/login
Log in to the application and receive a JWT token.

Food Items
GET /food
Retrieve a list of all food items.

GET /food/{id}
Retrieve details for a specific food item by its ID.

POST /food
Create a new food item (requires admin role).

PUT /food/{id}
Update an existing food item (requires admin role).

DELETE /food/{id}
Delete a food item (requires admin role).

Reviews
POST /reviews
Create a new review for a food item.

GET /reviews/{food_id}
Retrieve all reviews for a specific food item.

Orders (New Endpoint)
POST /orders
Create a new order with selected food items.

GET /orders/{id}
Retrieve order details by order ID.

User Stories
As a User:
I can create an account and log in to access the app.
I can view a list of all available food items.
I can leave reviews for food items.
I can order food items and track my orders.
As an Admin:
I can create, update, or delete food items.
I can view all orders placed by users.
