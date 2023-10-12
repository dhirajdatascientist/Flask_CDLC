Let's Add another microservice called `task_service`. This new service will allow users to add tasks and retrieve the list of tasks.

### Task Service Microservice:

#### Step 1: Setup

1. Create a new folder named `task_service` alongside your `greeting_service` folder.
2. Inside this folder, create a file named `app.py`.

#### Step 2: Create the Task Service

Open `app.py` in your favorite editor and add the following code:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory store for tasks
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if not task:
        return jsonify({"error": "Task not provided"}), 400

    tasks.append(task)
    return jsonify({"message": "Task added!"}), 201

if __name__ == '__main__':
    app.run(port=5001)
```

#### Step 3: Run the Service

1. Navigate to the `task_service` folder in your terminal.
2. Run the service using:
   ```bash
   python app.py
   ```
3. This will start the service on port 5001.

#### Step 4: Test Your Service

1. **Add a Task**: Use a tool like `curl` or Postman to add a task:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"task": "Learn Flask"}' http://localhost:5001/tasks
   ```
   This should return `{"message": "Task added!"}`.

2. **Retrieve Tasks**: In your browser or using `curl`, access the service:
   ```
   http://localhost:5001/tasks
   ```
   This should return the list of tasks, e.g., `["Learn Flask"]`.

#### Interacting between Microservices:

To make our example a bit more interesting, let's imagine you want the `greeting_service` to also tell the user about the number of tasks they have.

Modify the `greeting_service`'s `app.py` to include:

```python
import requests  # Add this to the top of your file

# ... rest of your code ...

@app.route('/greet_with_tasks/<name>', methods=['GET'])
def greet_with_tasks(name):
    response = requests.get("http://localhost:5001/tasks")
    number_of_tasks = len(response.json())
    return f"Hello, {name}! You have {number_of_tasks} tasks."
```

Ensure you have installed `requests` library using:

```bash
pip install requests
```

Now, when you access `http://localhost:5000/greet_with_tasks/John`, it will greet John and also tell him the number of tasks he has.

### Conclusion:

This example showcases two microservices (`greeting_service` and `task_service`) and how they can interact. In a real-world application, you'd have more robust communication, error handling, data storage, and possibly an event-driven mechanism for the services to communicate asynchronously.