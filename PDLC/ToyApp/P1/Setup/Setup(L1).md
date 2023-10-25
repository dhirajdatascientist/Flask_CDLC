### 🌟 Setting Up a Flask Environment on Windows 🌟

### 1️⃣ **Setting Up A Virtual Environment with `venv`**

1. **Open Command Prompt**:
    - Use the shortcut `Windows + R`, type `cmd`, and press `Enter`.

2. **Navigate to Your Project Directory**:
    ```bash
    mkdir toyapp
    cd toyapp
    ```

3. **Create the Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**:
    ```bash
    .\venv\Scripts\activate
    ```

   📝 **Note**: Once activated, you should see `(venv)` to the left of your command prompt, indicating the virtual environment is active.

---

### 2️⃣ **Installing Flask**

1. **Install Flask**:
    ```bash
    pip install Flask
    ```

2. **Verify Flask Installation**:
    ```bash
    python -m flask --version
    ```

---

### 3️⃣ **Creating and Running Your First Flask App**

1. **Create `app.py`**:
    - Use a text editor or IDE to create a new file named `app.py` in your project directory.
    - Add the following code to `app.py`:
      ```python
      from flask import Flask
      app = Flask(__name__)

      @app.route('/')
      def hello_world():
          return 'Hello, World!'

      if __name__ == '__main__':
          app.run(debug=True)
      ```

    📝 **Note**: The `if __name__ == '__main__':` line ensures that the Flask app only runs when this script is executed directly, and not if it's imported elsewhere.

2. **Run the Flask App**:
    - Ensure you're still in your project directory and your virtual environment is active.
    - Run the following command:
      ```bash
      python app.py
      ```

3. **Access Your Flask App**:
    - Open any web browser and navigate to:
      ```
      http://127.0.0.1:5000/
      ```
    - You should see the message: "Hello, World!"

---

🌟 **Wrap Up**: When done working on your Flask project, deactivate your virtual environment:
```bash
deactivate
```

Now you have a basic Flask setup where you can simply run `python app.py` to start your application. Happy coding! 🚀