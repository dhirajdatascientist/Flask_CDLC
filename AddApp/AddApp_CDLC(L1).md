# AddApp


```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = 1 + 2
    return f'1+2={result}'

app.run()
```
