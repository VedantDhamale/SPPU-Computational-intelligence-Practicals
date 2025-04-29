from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
       
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")
server.register_function(factorial, "compute_factorial")
server.serve_forever()



# ### **Explanation of the Code**
# This code sets up an **XML-RPC server** that listens on `localhost:8000` and provides two remote functions: `print_hello` and `factorial`.

# ---

# ### **Code Breakdown**
# 1. **Importing Required Module**  
#    ```python
#    from xmlrpc.server import SimpleXMLRPCServer
#    ```
#    - Imports `SimpleXMLRPCServer`, which allows the creation of an XML-RPC server.

# 2. **Defining Remote Functions**  
#    - **Function to return a greeting message**  
#      ```python
#      def print_hello(name=''):
#          return 'Hello ' + name
#      ```
#      - Accepts a `name` as input and returns `"Hello <name>"`.

#    - **Function to compute factorial**  
#      ```python
#      def factorial(n):
#          fact = 1
#          for i in range(1, n + 1):
#              fact *= i
#          return fact
#      ```
#      - Computes and returns the factorial of `n` using a loop.

# 3. **Creating and Configuring the Server**  
#    ```python
#    server = SimpleXMLRPCServer(("localhost", 8000))
#    ```
#    - Creates an XML-RPC server that listens on **localhost** at **port 8000**.

# 4. **Server Status Message**  
#    ```python
#    print("Listening on port 8000...")
#    ```
#    - Prints a message indicating that the server is running.

# 5. **Registering Functions for Remote Access**  
#    ```python
#    server.register_multicall_functions()
#    ```
#    - Enables **multi-call support**, allowing clients to make multiple calls in one request.

#    ```python
#    server.register_function(print_hello, "print_hello")
#    server.register_function(factorial, "Factorial")
#    ```
#    - Registers the functions `print_hello` and `factorial` so that clients can call them remotely.

# 6. **Starting the Server**  
#    ```python
#    server.serve_forever()
#    ```
#    - Runs the server indefinitely, waiting for client requests.

# ---

# ### **Viva Questions and Answers**
# #### **1. What is the purpose of `SimpleXMLRPCServer`?**  
# **Ans:** It creates an XML-RPC server that allows clients to call registered functions remotely.

# #### **2. What does `server.serve_forever()` do?**  
# **Ans:** It starts the server and keeps it running, listening for incoming requests.

# #### **3. How does `server.register_function()` work?**  
# **Ans:** It registers a function so that it can be accessed remotely by XML-RPC clients.

# #### **4. Why do we use `server.register_multicall_functions()`?**  
# **Ans:** It enables the server to process multiple function calls in a single request.

# #### **5. What is the role of `"localhost", 8000` in `SimpleXMLRPCServer(("localhost", 8000))`?**  
# **Ans:** It binds the server to the local machine (`localhost`) and listens for requests on port `8000`.

# #### **6. What is XML-RPC used for?**  
# **Ans:** XML-RPC is used for remote procedure calls over HTTP using XML-based encoding.

# #### **7. How does `print_hello(name)` function work?**  
# **Ans:** It returns `"Hello <name>"`, where `<name>` is the input given by the client.

# #### **8. How does the `factorial(n)` function work?**  
# **Ans:** It calculates the factorial of `n` using a loop and returns the result.

# #### **9. What happens if the server is not running?**  
# **Ans:** The client will fail to connect and throw a connection error.

# #### **10. How can you stop the server?**  
# **Ans:** By pressing **Ctrl + C** in the terminal or manually terminating the process.