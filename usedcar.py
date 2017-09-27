from idea.car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    limo = Car(100, "limo")
    limo.add_fuel(20)
    print("fuel = ", limo.fuel)
    limo.drive(115)
    print("odo = ", limo.odometer)
    print(limo)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))


main()
