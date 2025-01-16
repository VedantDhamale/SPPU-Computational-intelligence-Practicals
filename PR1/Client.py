import xmlrpc.client
n=int(input('Enter the value of n:'))
with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("Printing: %s" % str(proxy.print_hello('Atharva')))
    print(f"Fatcorial of {n}: %s" % str(proxy.Factorial(n)))
