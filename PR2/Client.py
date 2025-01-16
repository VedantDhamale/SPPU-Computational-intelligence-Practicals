import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

try:
    result = server.concat(string1, string2)
    print(f"Concatenated String: {result}")
except Exception as e:
    print(f"An error occurred: {e}")