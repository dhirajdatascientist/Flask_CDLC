To add an "Add to Cart" button for each product, you can utilize Bootstrap's button component within the product cards in the `product.html` template.

Let's enhance our previous code by adding the button:

### 🌟 **Adding "Add to Cart" Button to Products** 🌟

1️⃣ **Modify the `product.html` Template**:

Inside the `templates` folder, update `product.html`:

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
                <button class="btn btn-primary">Add to Cart</button> <!-- Add to Cart Button -->
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
                <button class="btn btn-primary">Add to Cart</button> <!-- Add to Cart Button -->
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
                <button class="btn btn-primary">Add to Cart</button> <!-- Add to Cart Button -->
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

The key addition here is:
```html
<button class="btn btn-primary">Add to Cart</button>
```
This Bootstrap-styled button will show up below each product's price in the card.

2️⃣ **Run the Application**:

Ensure your virtual environment (`venv`) is active and run the Flask app:
```bash
python app.py
```

3️⃣ **Access the Product Page**:

Open a web browser and navigate to:
```
http://127.0.0.1:5000/product
```

Now, below each product's price, you'll see an "Add to Cart" button. In a full-fledged e-commerce application, clicking this button would typically add the product to a shopping cart, but that involves more backend logic. For now, the button serves as a visual placeholder.