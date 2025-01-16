from xmlrpc.server import SimpleXMLRPCServer

def print_hello(name=''):
    return 'Hello '+name

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
       
server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(print_hello, "print_hello")
server.register_function(factorial,'Factorial')
server.serve_forever()