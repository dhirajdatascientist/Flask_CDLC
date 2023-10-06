To change the port in Flask, you can use one of the following methods:

**Method 1: Pass the port argument to the app.run() method**

When you start your Flask application using the `flask run` command, the default port is 5000. You can change the port by passing the `port` argument to the `app.run()` method. For example, to start your application on port 8000, you would use the following command:

```python
from flask import Flask

app = Flask(__name__)

# Your routes and application logic here

if __name__ == "__main__":
    # Change the port by specifying the `port` parameter
    app.run(host="0.0.0.0", port=8080)  # Change 8080 to your desired port number

```

**Method 2: Set the FLASK_RUN_PORT environment variable**

You can also set the port for your Flask application by setting the `FLASK_RUN_PORT` environment variable. For example, to set the port to 8000, you would use the following command:

```
export FLASK_RUN_PORT=8000
```

**Method 3: Set the SERVER_NAME config variable**

You can also set the port for your Flask application by setting the `SERVER_NAME` config variable. This variable should be set to the fully qualified domain name (FQDN) or IP address of the server where your application is running, followed by a colon and the port number. For example, to set the port to 8000, you would add the following line to your application's config file:

```
SERVER_NAME = example.com:8000
```

Once you have changed the port, you will need to restart your Flask application. You can then access your application at the new port. For example, if you changed the port to 8000, you would access your application at `http://localhost:8000`.

**Note:** If you are running your Flask application on a production server, you should not use the `flask run` command. Instead, you should use a production WSGI server such as uWSGI or Gunicorn. These servers will allow you to configure the port for your application and run it in a more efficient and secure manner.