class Vehicle :
    type = ""
    licenceNumber = ""
    serialNumber = ""
    face = ""
    def turnOnAir(self):
        print(self.type, "Turn on : air")
class Pickup(Vehicle) :
    pass
class Car(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

pickup = Pickup()
pickup.type = "Pickup"
pickup.turnOnAir()
car = Car()
car.type = "Car"
car.turnOnAir()
van = Van()
van.type = "Van"
van.turnOnAir()
estatecar = Estatecar()
estatecar.type = "Estatecar"
estatecar.turnOnAir()
