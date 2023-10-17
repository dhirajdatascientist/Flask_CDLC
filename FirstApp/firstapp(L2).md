## FirstApp(L2)

1. **Route Addition:** Write a new route called `/greet/<name>`, where `<name>` is a variable. The route should return "Hello `<name>`" where `<name>` is the name passed in the URL.

2. **Method Restriction:** Modify the `/sagar` route to only allow the `POST` method. 

3. **JSON Response:** Update the `/varsha` route to return a JSON response with keys `name` and `message`. The response should look like this: `{"name": "Varsha", "message": "Hello Varsha"}`.

4. **Query Parameters:** Create a new route called `/hello` that accepts a query parameter named `name`. If the name is provided, it should return "Hello `<name>`". If no name is provided, it should return "Hello Guest".

5. **Error Handling:** Add error handling to the Flask app to return "Route not found" for any undefined routes (404 error).

6. **Route Redirection:** Implement a route `/redirect` that redirects the user to the `/sagar` route.

7. **Static Files:** Add a static route that serves an image file from a directory named `static`. Name the route `/image` and serve an image called `pic.jpg`.

8. **Template Rendering:** Instead of returning "Hello Sagar" as plain text from the `/sagar` route, render an HTML template that displays the message in a header tag.

9. **Form Submission:** Create a route `/submit` that displays a form with an input field for a name. Upon submission, it should redirect to the `/greet/<name>` route, displaying the greeting message with the provided name.

10. **Database Integration:** Integrate a SQLite database with the Flask app. Create a route `/add/<name>` that adds the provided name to a table called `users`. Also, create a route `/all` that lists all the names added to the database.