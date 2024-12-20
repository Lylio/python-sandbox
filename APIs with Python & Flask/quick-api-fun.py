from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data store (in-memory, for simplicity)
items = [
    {"id": 1, "name": "Item One", "description": "This is the first item"},
    {"id": 2, "name": "Item Two", "description": "This is the second item"}
]


# Helper function to find item by ID
def find_item(item_id):
    return next((item for item in items if item['id'] == item_id), None)


# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200


# Route to get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


# Route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if 'name' not in data or 'description' not in data:
        return jsonify({"error": "Name and description are required"}), 400

    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,  # Auto-increment ID
        "name": data['name'],
        "description": data['description']
    }
    items.append(new_item)
    return jsonify(new_item), 201


# Route to update an existing item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    item['name'] = data.get('name', item['name'])  # Update only if new value is provided
    item['description'] = data.get('description', item['description'])
    return jsonify(item), 200


# Route to delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = find_item(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404

    items.remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
