#Client
import Pyro5.api

hotel = Pyro5.api.Proxy("PYRONAME:hotel.service")

while True:
    print("\n1. Book Room\n2. Cancel Booking\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        print(hotel.book(name))
    elif choice == "2":
        name = input("Enter name: ")
        print(hotel.cancel(name))
    elif choice == "3":
        print(hotel.display())
    elif choice=='4':
        break