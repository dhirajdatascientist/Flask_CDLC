# Test your skill

1. Implement error handling in a Flask REST API so that it returns a custom error message when an invalid endpoint is accessed.

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Custom error handler for invalid endpoints
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

# Route for a valid endpoint
@app.route('/api/resource/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    # Your code to retrieve the resource goes here
    return jsonify({'message': 'Resource found', 'resource_id': resource_id})

if __name__ == '__main__':
    app.run(debug=True)
```