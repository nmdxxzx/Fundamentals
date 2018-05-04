class Car:
    brand = "no brand"
    maxSpeed = 0
    def setBrand(self,brand_name):
        self.brand = brand_name
    def setMaxspeed(self,max_speed):
        self.maxSpeed = max_speed
    def printData(self):
        print("The car's brand is:",self.brand)
        print("The maximum speed of the car is", self.maxSpeed, "km/h")

c1 = Car()
c1.setBrand("Audi")
c1.setMaxspeed(200)
c1.printData()
