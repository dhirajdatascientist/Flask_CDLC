### Step 1: Create a Simple Flask Application
Let's create a very basic Flask app. You'll need two files: `app.py` to hold your application code, and `requirements.txt` to list your Python dependencies.

#### app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

#### requirements.txt
```
Flask==2.0.2
```

### Step 2: Create a Dockerfile
Create a `Dockerfile` in the same directory as your Flask application to define how the app should be containerized.

#### Dockerfile
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME DockerFlask

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### Step 3: Build Docker Image and Run the Container
1. **Build Docker Image:** In the directory containing your `app.py`, `requirements.txt`, and `Dockerfile`, run the following command to build your Docker image, replacing `myflaskapp` with whatever name you choose for your image:
   ```shell
   docker build -t myflaskapp .
   ```
   
2. **Run Docker Container:** Once the image is built, you can start a container from that image. Map port `5000` in the container to a port on your host (e.g., `5000`) so that you can access the app.
   ```shell
   docker run -p 5000:5000 myflaskapp
   ```

### Step 4: Access the Flask App in Browser
Open a web browser and navigate to `http://localhost:5000/`. You should see "Hello, Docker!" displayed in your browser.

### Additional Notes:
- Ensure you have Docker installed and running on your machine to use the Docker commands.
- Adjust versions in `requirements.txt` according to your project's needs.
- Ensure your app has no errors before attempting to containerize it.
- The security settings in this example are suitable for development but not for production. Consider using a production-ready server (like Gunicorn) and take additional security measures for a production environment.