# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.
#
# Create five different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

class car(object):
    def __init__(self, price, speed, fuel, miles):
        self.price = price
        self.speed = speed
        self.miles = miles
        self.fuel = fuel
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Miles: " + str(self.miles)
        print "Tax: " + str(self.tax)

Honda = car(1100, '40mph', 'Full', '25mpg')
Toyota = car(2000, '35mph', 'Not Full', '45mpg')
Ford= car(2500, '20mph', 'Half Full', '50mpg')
Chevrolet= car(2100, '50mph', 'Full', '10mpg')
Tesla= car(80000, '60mph', 'N/A', '90mpg')
