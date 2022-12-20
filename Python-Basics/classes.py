# This a demo of class generating 
# This is a flight program

class Flight():
    #function 1 for capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    #function 2 for passenger
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    #function 3 for seats
    def open_seats(self):
        return self.capacity -len(self.passengers)
flight =Flight(3)
        
#Let us assume the list of the passengers
people = ["Ali", "Mahmut", "Cevdet", "Yasar"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")    