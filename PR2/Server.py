
import Pyro5.api
@Pyro5.api.expose
class Concatenator:
    def concat(self, a, b):
        return a + b
daemon = Pyro5.api.Daemon()
uri = daemon.register(Concatenator)
print("Server is ready. URI:", uri)
daemon.requestLoop()