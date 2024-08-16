from flask import Blueprint, jsonify, request

# Create a Blueprint with a custom name
product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
def get_products():
    # Placeholder for logic to retrieve all products
    return jsonify([])  # Returns an empty list as a placeholder

@product_routes.route('/products', methods=['POST'])
def add_product():
    data = request.json
    # Placeholder for logic to add a new product
    return jsonify({"message": "Product added successfully", "product": data}), 201

@product_routes.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Placeholder for logic to retrieve a specific product by ID
    return jsonify({"id": product_id})  # Returns the product ID as a placeholder

@product_routes.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    # Placeholder for logic to update a product by ID
    return jsonify({"message": "Product updated successfully", "product_id": product_id, "updated_data": data})

@product_routes.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Placeholder for logic to delete a product by ID
    return jsonify({"message": f"Product {product_id} deleted successfully"})
