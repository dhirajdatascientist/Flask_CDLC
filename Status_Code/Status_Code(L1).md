## HTTP status codes

HTTP status codes are three-digit numbers that indicate the outcome of an HTTP request made by a client (like a web browser) to a server. They provide information about whether the request was successful, encountered an error, or needs further action. Here are some common HTTP status codes explained in simple terms:

1. **1xx (Informational)**: These are informational responses, indicating that the request was received and understood. They don't usually require any action from the client.
   - **100 - Continue**: The server has received the request headers and the client can proceed with the request body.

2. **2xx (Success)**: These codes indicate that the request was successful and the server was able to fulfill it.
   - **200 - OK**: The request was successful, and the server sends the requested data.
   - **201 - Created**: The request has been fulfilled, and a new resource has been created.
   - **204 - No Content**: The request was successful, but there is no data to send back (often used in DELETE requests).

3. **3xx (Redirection)**: These codes indicate that the client needs to take further action to complete the request.
   - **301 - Moved Permanently**: The requested resource has permanently moved to a new location.
   - **302 - Found**: The requested resource has temporarily moved to a different location.
   - **304 - Not Modified**: The client's cached copy of the resource is still valid; no need to download it again.

4. **4xx (Client Error)**: These codes indicate that there was an issue with the client's request.
   - **400 - Bad Request**: The request is invalid or malformed.
   - **401 - Unauthorized**: Authentication is required to access the resource.
   - **403 - Forbidden**: The client is authenticated but doesn't have permission to access the resource.
   - **404 - Not Found**: The requested resource could not be found on the server.

5. **5xx (Server Error)**: These codes indicate that there was an issue on the server's side.
   - **500 - Internal Server Error**: Something went wrong on the server that prevented it from fulfilling the request.
   - **502 - Bad Gateway**: The server, while acting as a gateway or proxy, received an invalid response from the upstream server.
   - **503 - Service Unavailable**: The server is temporarily unable to handle the request due to maintenance or overload.

These status codes help both clients and servers communicate about the outcome of HTTP requests, making it easier to troubleshoot and handle different situations when interacting with web services.