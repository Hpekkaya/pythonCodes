# Define the Car class
class Car:
    # The __init__ method is called when a new instance of the class is created.
    # It initializes the attributes of the class.
    def __init__(self, make, model, year):
        # Instance variables unique to each instance
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # A default value for all new cars

    # Method to describe the car
    def describe_car(self):
        # Returns a neatly formatted descriptive name for the car
        return f"{self.year} {self.make} {self.model}"

    # Method to read the car's odometer
    def read_odometer(self):
        # Prints the car's mileage
        print(f"This car has {self.odometer_reading} miles on it.")

    # Method to update the odometer reading
    # Here we add logic to prevent rolling back the odometer
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Method to increment the odometer reading
    def increment_odometer(self, miles):
        if miles < 0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles


# Creating an instance of the Car class
my_car = Car("Tesla", "Model s", 2020)

# Accessing attributes
print(my_car.describe_car())
my_car.read_odometer()

# Updating and reading the odometer
my_car.update_odometer(23)
my_car.read_odometer()

# Incrementing the odometer
my_car.increment_odometer(100)
my_car.read_odometer()
