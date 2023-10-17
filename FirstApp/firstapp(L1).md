```python
from flask import Flask
app = Flask(__name__)


@app.route('/sagar')
def sagar():
    return "Hello Sagar"

@app.route('/varsha')
def varsha():
    return "Hello Varsha"

app.run()
```