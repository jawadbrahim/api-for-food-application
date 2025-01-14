from flask import Blueprint, jsonify

# Create a mock API blueprint
mock_api_bp = Blueprint('mock_api', __name__)

# Mock endpoint for POST /foods (Create food)
@mock_api_bp.route('/foods', methods=['POST'])
def create_food():
    return jsonify({
        "id": 1,
        "category": "Dessert",
        "title": "Chocolate Cake",
        "description": "A delicious chocolate cake.",
        "picture": "http://example.com/image.jpg",
        "ingredients": "Flour, sugar, chocolate"
    }), 201

# Mock endpoint for GET /foods/{food_id} (Get food details)
@mock_api_bp.route('/foods/<int:food_id>', methods=['GET'])
def get_food(food_id):
    return jsonify({
        "id": food_id,
        "category": "Dessert",
        "title": "Chocolate Cake",
        "description": "A delicious chocolate cake.",
        "picture": "http://example.com/image.jpg",
        "ingredients": "Flour, sugar, chocolate"
    }), 200

# Mock endpoint for PUT /foods/{food_id} (Update food details)
@mock_api_bp.route('/foods/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    return jsonify({
        "id": food_id,
        "category": "Dessert",
        "title": "Chocolate Cake",
        "description": "An updated description of the chocolate cake.",
        "picture": "http://example.com/image.jpg",
        "ingredients": "Flour, sugar, chocolate, vanilla"
    }), 200

# Mock endpoint for DELETE /foods/{food_id} (Delete food item)
@mock_api_bp.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    return jsonify({"message": f"Food item {food_id} deleted successfully."}), 200
