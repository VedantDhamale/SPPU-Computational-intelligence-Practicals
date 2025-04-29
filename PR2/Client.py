
#Client
import Pyro5.api
uri = input("Enter server URI: ")
server = Pyro5.api.Proxy(uri)
a = input("Enter first string: ")
b = input("Enter second string: ")
result = server.concat(a, b)
print("Result:", result)