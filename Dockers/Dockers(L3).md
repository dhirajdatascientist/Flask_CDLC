### Prerequisite: Install Docker
Ensure Docker is installed on your system. If not, download and install it from [Docker's official site](https://www.docker.com/products/docker-desktop).

### Step 1: Create a Simple Flask Application
#### 1.1 Setup a new directory
Create a new directory for your project and navigate into it:
```shell
mkdir myflaskapp
cd myflaskapp
```
#### 1.2 `app.py`
Create a file named `app.py` with the following content:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```
#### 1.3 `requirements.txt`
Create a file named `requirements.txt`:
```plaintext
Flask==2.0.2
```

### Step 2: Create a Dockerfile
#### 2.1 Create Dockerfile
In the same directory, create a file named `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
ENV NAME DockerFlask
CMD ["python", "app.py"]
```

### Step 3: Build Docker Image and Run the Container
#### 3.1 Open Terminal
Navigate to the directory containing `app.py`, `requirements.txt`, and `Dockerfile` in your terminal.

#### 3.2 Build Docker Image
```shell
docker build -t myflaskapp .
```
#### 3.3 Run Docker Container
```shell
docker run -p 5000:5000 myflaskapp
```
### Step 4: Access the Flask App in Browser
#### 4.1 Open Browser
Navigate to [http://localhost:5000/](http://localhost:5000/). You should see "Hello, Docker!" on the webpage.

### Additional Notes:
- **Troubleshooting Docker:** Ensure Docker is running before executing Docker commands.
- **Flask Version:** Update the Flask version in `requirements.txt` as needed.
- **App Error Checking:** Confirm your app runs without errors in a local environment before Dockerizing.
- **Security and Production:** This setup is not production-ready. For deployment, use a production WSGI server, such as Gunicorn, and implement additional security practices.

### Conclusion
This step-by-step guide allows you to Dockerize a basic Flask application. For larger applications or deployment, additional configurations and optimizations will be necessary.