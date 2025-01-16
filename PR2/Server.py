from xmlrpc.server import SimpleXMLRPCServer

def concat_string(str1,str2):
    return str1 + str2

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_multicall_functions()
server.register_function(concat_string, "concat")
server.serve_forever()