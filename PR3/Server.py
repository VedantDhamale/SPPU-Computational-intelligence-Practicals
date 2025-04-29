#HotelRoom
#Server
import Pyro5.api
@Pyro5.api.expose
class Hotel:
    def __init__(self):
        self.bookings = {}

    def book(self, name):
        if name in self.bookings:
            return f"{name} already has a booking."
        self.bookings[name] = f"Room #{len(self.bookings) + 1}"
        return f"Room booked for {name}."

    def cancel(self, name):
        if name in self.bookings:
            del self.bookings[name]
            return f"Booking cancelled for {name}."
        return f"No booking found for {name}."
    
    def display(self):
        return self.bookings

daemon = Pyro5.api.Daemon()
uri = daemon.register(Hotel)
print("URI:", uri)

ns = Pyro5.api.locate_ns()
ns.register("hotel.service", uri)

print("Hotel Booking Server is running...")
daemon.requestLoop()