### Implementing a Microservice in Flask:

Let's create a  Microservice using Flask which returns a greeting message.

#### Step 1: Setup

1. **Install Python**: If you haven't already, install Python.
2. **Install Flask**: Use pip to install Flask:
   ```bash
   pip install Flask
   ```

#### Step 2: Create Your First Service

1. Create a new folder named `greeting_service`.
2. Inside this folder, create a file named `app.py`.
3. Open `app.py` in your favorite editor and add the following code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(port=5000)
```

#### Step 3: Run the Service

1. Navigate to the `greeting_service` folder in your terminal.
2. Run the service using:
   ```bash
   python app.py
   ```
3. This will start the service on port 5000.

#### Step 4: Test Your Service

1.Using `Postman`:

- Download and install `Postman`.
- Open `Postman`.
- Click on `new`
- Select `post`
- To retrieve all tasks, 
   - Set the request type to GET and enter the URL http://127.0.0.1:5001/tasks, then click "Send".

- To add a new task, 
   - Set the request type to POST
   - Enter the URL http://127.0.0.1:5001/tasks, 
   - Go to the "Body" tab
   - Select "raw" and "JSON (application/json)", 
   - and enter a JSON body like {"task": "Do laundry"}, 
   - then click "Send".


## To add multiple tasks without modifying the API:

1. Using Postman:
   
   - Open Postman.
   - Set the request type to POST.
   - Enter the URL http://127.0.0.1:5001/tasks.
   - Go to the "Body" tab, select "raw" and "JSON (application/json)".
   
   - To add the first task:
     - Enter the JSON payload, for example, {"task": "Do laundry"}.
     - Click "Send".
   
   - To add the second task:
     - Change the payload, for instance, to {"task": "Buy groceries"}.
     - Click "Send" again.

   - Repeat the process for any additional tasks.

2. Using the Collection Runner in Postman:
   
   If you want to automate the sending of multiple tasks in Postman, you can use the Collection Runner:

   - Create a collection in Postman.
   - Add your request to the collection.
   - Use the Collection Runner to run the request multiple times, each time with a different task payload.

This method uses the original API code without any modification. Each task is still being added with an individual POST request, but you're manually changing the payload for each one.

Now let's go for Microservices(L3)