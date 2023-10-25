Add a 5-star rating system to each product. For simplicity, we'll use an HTML and CSS approach, without any interactive functionality. This will provide a static display of product ratings.

### 🌟 **Adding 5-Star Rating to Products** 🌟

1️⃣ **Modify the `product.html` Template**:

Inside the `templates` folder, update `product.html` to include the rating:

Add the following style to the top of the template to represent the stars:

```html
<style>
    .stars {
        display: inline-block;
    }
    
    .star {
        font-size: 20px;
        color: #ddd; /* default star color */
    }
    
    .filled {
        color: gold; /* filled star color */
    }
</style>
```

For each product, you can add the following star rating system just before the price:

```html
<div class="stars">
    <span class="star filled">&#9733;</span>
    <span class="star filled">&#9733;</span>
    <span class="star filled">&#9733;</span>
    <span class="star">&#9733;</span>
    <span class="star">&#9733;</span>
</div>
```

This example displays a 3 out of 5-star rating. Adjust the number of `.filled` classes to represent the desired rating for each product.

2️⃣ **Enhanced Product Display**:

With this change, each product card in the `product.html` file will now have a star rating just above the product's price. The rating is static, and you've set it to 3 out of 5 for demonstration purposes. Adjust it as needed for each product.

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

Now, above each product's price and below its name, you'll see a star rating. Adjust the rating by changing the number of filled stars as per your needs.

In a more advanced setting, you'd integrate this with a backend to dynamically fetch and display product ratings based on user reviews or other metrics.