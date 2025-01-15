import rpyc

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)

class FactorialService(rpyc.Service):
    def exposed_calculate_factorial(self, n):
        return Factorial(n)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(FactorialService, port=18861)
    print("Server is running...")
    server.start()