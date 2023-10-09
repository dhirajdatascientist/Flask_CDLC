# Problem Statements:

### 001_Requirement:
Design and build a RESTful API for a food ordering system using Flask. 

### 002_Requirement:
Create a list of food items with attributes `id`, `name`, and `price`, and expose CRUD (Create, Read, Update, Delete) operations for these items through the API.


# Solution_Steps

```
pip install flask
```

Now, create a Python script (e.g., `app.py`) with the following code:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for food items
food_items = [
    {"id": 1, "name": "Burger", "price": 5.99},
    {"id": 2, "name": "Pizza", "price": 8.99},
    {"id": 3, "name": "Pasta", "price": 7.49},
]

# Route to get all food items
@app.route('/food', methods=['GET'])
def get_food_items():
    return jsonify(food_items)

# Route to get a specific food item by ID
@app.route('/food/<int:item_id>', methods=['GET'])
def get_food_item(item_id):
    item = next((item for item in food_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Food item not found"}), 404
    return jsonify(item)

# Route to add a new food item
@app.route('/food', methods=['POST'])
def add_food_item():
    new_item = request.get_json()
    if not new_item or 'name' not in new_item or 'price' not in new_item:
        return jsonify({"error": "Invalid data"}), 400

    # Generate a new unique ID
    new_id = max(item['id'] for item in food_items) + 1
    new_item['id'] = new_id
    food_items.append(new_item)
    return jsonify(new_item), 201

# Route to update a food item by ID
@app.route('/food/<int:item_id>', methods=['PUT'])
def update_food_item(item_id):
    updated_item = request.get_json()
    if not updated_item or 'name' not in updated_item or 'price' not in updated_item:
        return jsonify({"error": "Invalid data"}), 400

    item = next((item for item in food_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Food item not found"}), 404

    item['name'] = updated_item['name']
    item['price'] = updated_item['price']
    return jsonify(item)

# Route to delete a food item by ID
@app.route('/food/<int:item_id>', methods=['DELETE'])
def delete_food_item(item_id):
    item = next((item for item in food_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Food item not found"}), 404

    food_items.remove(item)
    return jsonify({"message": "Food item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
```

In this project:

- We define routes for listing all food items, getting a specific food item by ID, adding a new food item, updating an existing food item, and deleting a food item.

- The `food_items` list holds sample data for food items.

- We use the `Flask` framework to create the API endpoints and handle HTTP requests.

To run the Flask application, save the code above to a file (e.g., `app.py`) and run it with:

```
python app.py
```

Your RESTful API for managing food items will be available at the following endpoints:

- `GET /food`: Get a list of all food items.
- `GET /food/<item_id>`: Get a specific food item by ID.
- `POST /food`: Add a new food item.
- `PUT /food/<item_id>`: Update a food item by ID.
- `DELETE /food/<item_id>`: Delete a food item by ID.

You can test these endpoints using tools like `curl` or Postman, or by creating a front-end application to interact with the API.