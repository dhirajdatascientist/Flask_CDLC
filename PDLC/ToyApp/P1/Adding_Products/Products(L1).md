### 🌟 **Adding Sample Products to the Product Page** 🌟

#### 1️⃣ **Directory Structure**:

Add a new `static` folder to store the sample product images:

```
your_project_directory/
│
├── static/
│   ├── product1.jpg
│   ├── product2.jpg
│   └── product3.jpg
├── templates/
│   ├── base.html
│   ├── product.html
│   ├── services.html
│   └── contact.html
└── app.py
```

Let's assume you have 3 product images named `product1.jpg`, `product2.jpg`, and `product3.jpg` inside the `static` folder.

#### 2️⃣ **Updating the Product Template**:

Inside the `templates` folder, modify `product.html`:

```html
{% extends "base.html" %}

{% block content %}
<h2>Our Toys</h2>

<div class="row">
    <!-- Product 1 -->
    <div class="col-md-4">
        <div class="card mb-4">
            <img src="{{ url_for('static', filename='product1.jpg') }}" class="card-img-top" alt="Toy 1">
            <div class="card-body">
                <h5 class="card-title">Toy 1</h5>
                <p class="card-text">$10.99</p>
            </div>
        </div>
    </div>

    <!-- Product 2 -->
    <div class="col-md-4">
        <div class="card mb-4">
            <img src="{{ url_for('static', filename='product2.jpg') }}" class="card-img-top" alt="Toy 2">
            <div class="card-body">
                <h5 class="card-title">Toy 2</h5>
                <p class="card-text">$12.99</p>
            </div>
        </div>
    </div>

    <!-- Product 3 -->
    <div class="col-md-4">
        <div class="card mb-4">
            <img src="{{ url_for('static', filename='product3.jpg') }}" class="card-img-top" alt="Toy 3">
            <div class="card-body">
                <h5 class="card-title">Toy 3</h5>
                <p class="card-text">$14.99</p>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

#### 3️⃣ **Running the Application**:

1. Ensure your virtual environment (`venv`) is still active.
2. Run the Flask app:
    ```bash
    python app.py
    ```

3. **Access the Product Page**:

Open a web browser and navigate to:

```
http://127.0.0.1:5000/product
```

You should now see the Product page showcasing three sample toy products using Bootstrap cards. Each card will display the product image, name, and price. Adjust the product details and images as needed for your actual products.