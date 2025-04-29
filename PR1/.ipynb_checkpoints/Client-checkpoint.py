import xmlrpc.client
n=int(input('Enter the value of n:'))
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("Printing: %s" % str(proxy.print_hello('Vedant')))
    print(f"Fatcorial of {n}: %s" % str(proxy.Factorial(n)))


# ### **Explanation of the Code**
# The given Python code demonstrates how to use **XML-RPC (Remote Procedure Call using XML)** to communicate with a remote server and execute functions.

# #### **Code Breakdown**
# 1. **Importing xmlrpc.client**  
#    ```python
#    import xmlrpc.client
#    ```
#    - This module provides tools for making remote procedure calls using XML-RPC.

# 2. **Taking User Input**  
#    ```python
#    n = int(input('Enter the value of n:'))
#    ```
#    - The program prompts the user to enter an integer value `n`.

# 3. **Creating a Server Proxy**  
#    ```python
#    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
#    ```
#    - This creates a connection to an XML-RPC server running on `localhost` at port `8000`.
#    - The `proxy` object is used to call remote functions available on the server.

# 4. **Calling Remote Functions**  
#    ```python
#    print("Printing: %s" % str(proxy.print_hello('Vedant')))
#    ```
#    - Calls the remote function `print_hello` with the argument `'Vedant'`.
#    - The server processes this and returns a response, which is then printed.

#    ```python
#    print(f"Factorial of {n}: %s" % str(proxy.Factorial(n)))
#    ```
#    - Calls the remote function `Factorial(n)`, which computes the factorial of `n` on the server and returns the result.

# ---

# ### **Viva Questions and Answers**
# #### **1. What is XML-RPC?**  
# **Ans:** XML-RPC is a protocol that allows remote procedure calls using XML for data encoding and HTTP as the transport mechanism.

# #### **2. What does `xmlrpc.client.ServerProxy` do?**  
# **Ans:** `ServerProxy` is used to connect to a remote XML-RPC server and call its methods as if they were local functions.

# #### **3. What is the role of `localhost:8000` in the code?**  
# **Ans:** It specifies that the XML-RPC server is running on the local machine (`localhost`) on port `8000`.

# #### **4. What is the purpose of `proxy.print_hello('Vedant')`?**  
# **Ans:** It calls the `print_hello` function on the server, which likely returns a greeting message.

# #### **5. How does `proxy.Factorial(n)` work?**  
# **Ans:** It calls the `Factorial` function on the server, which computes and returns the factorial of `n`.

# #### **6. What are the advantages of XML-RPC?**  
# **Ans:**  
# - Platform-independent  
# - Simple to implement  
# - Uses HTTP, which is firewall-friendly  

# #### **7. What is the difference between XML-RPC and REST API?**  
# **Ans:**  
# - **XML-RPC**: Uses XML for requests and responses, and functions are called remotely.  
# - **REST API**: Uses HTTP methods (GET, POST, etc.) and supports multiple data formats like JSON.  

# #### **8. How can you start an XML-RPC server?**  
# **Ans:** Using Python’s `xmlrpc.server.SimpleXMLRPCServer` to define methods and run the server on a specified port.

# #### **9. What happens if the server is not running?**  
# **Ans:** The client will throw a connection error, as it won’t be able to communicate with the server.

# #### **10. Can XML-RPC handle complex data types?**  
# **Ans:** It supports basic data types like integers, strings, and lists but has limitations in handling complex objects directly.