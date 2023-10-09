### Some guidelines on when to use each method and when not to use them:

**When to Use GET:**

1. **Retrieving Data**: Use GET when you want to retrieve data from the server without causing any side effects. GET requests should not modify server state.

2. **Idempotent Operations**: GET requests are idempotent, meaning that making the same request multiple times should not have different outcomes. This makes them suitable for operations that should not change data.

3. **Caching**: GET requests can be cached by browsers and proxy servers, which can improve performance for frequently accessed resources.

4. **Bookmarkable URLs**: GET requests are suitable for creating bookmarkable URLs. Users can save and share URLs to return to specific content or pages.

5. **Safe and Stateless**: GET requests are safe and should not have any side effects on the server. They should also be stateless, meaning each request stands alone and does not rely on previous requests.

**When Not to Use GET:**

1. **Sensitive Data**: Avoid using GET for sending sensitive data like passwords or other confidential information. Data sent via GET is visible in the URL, and it can be logged in browser history, server logs, and potentially seen by third parties.

2. **Large Data**: GET requests are limited in the amount of data they can send because the data is included in the URL. If you need to send a large amount of data, use POST instead.

3. **State-Changing Operations**: Do not use GET for actions that change server state or have side effects. Use POST for such operations.

**When to Use POST:**

1. **Data Submission**: Use POST when you need to submit data to the server, such as when filling out forms, making a purchase, or submitting comments.

2. **Security**: POST is more secure than GET for sending sensitive information because the data is sent in the request body and is not visible in the URL.

3. **Large Data**: POST allows you to send larger amounts of data to the server because it's included in the request body, not in the URL.

4. **State-Changing Operations**: Use POST for actions that modify server state or have side effects, like creating, updating, or deleting records.

**When Not to Use POST:**

1. **Retrieval of Data**: Avoid using POST to retrieve data from the server. It's not the intended use, and it can lead to unexpected side effects if the server is not designed to handle retrieval via POST.

2. **Idempotent Operations**: POST requests are not idempotent by default, so avoid using them for operations that should not be repeated.

**Conclusion**
Choose GET for safe, read-only operations and use POST for actions that modify server state, involve sensitive data, or require sending large amounts of data. It's essential to follow these guidelines to ensure proper behavior and security in your web applications.