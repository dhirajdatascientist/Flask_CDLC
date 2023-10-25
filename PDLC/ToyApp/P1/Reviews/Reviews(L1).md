### 🌟 **Adding Reviews Display to Products** 🌟

1️⃣ **Modify the `product.html` Template**:

Add the following section after the "Add to Cart" button and before the end of the `card-body` for each product:

```html
<div class="reviews">
    <h6>Customer Reviews:</h6>
    <p>"Great toy! My kid loves it." - Alex</p>
    <p>"Good quality and timely delivery." - Sam</p>
    <p>"Could be better. Not worth the price." - Riley</p>
</div>
```

To make the reviews stand out a bit more, you can add some CSS styling. Add this style block at the top of the template:

```html
<style>
    .reviews {
        margin-top: 20px;
        border-top: 1px solid #eee;
        padding-top: 10px;
    }
    .reviews h6 {
        margin-bottom: 10px;
    }
</style>
```

2️⃣ **Enhanced Product Display**:

With this change, each product card in the `product.html` file will now display three static reviews after the "Add to Cart" button. These are just mock reviews for demonstration purposes.

3️⃣ **Run the Application**:

Ensure your virtual environment (`venv`) is active and run the Flask app:
```bash
python app.py
```

4️⃣ **Access the Product Page**:

Open a web browser and navigate to:
```
http://127.0.0.1:5000/product
```

Now, below the "Add to Cart" button for each product, you'll see some mock customer reviews.
