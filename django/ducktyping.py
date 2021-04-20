#methods are important than class
class Swift:
    def start(self):
        print("swift car start method")


    def accelerate(self):
        print("swift can accelerate")

    def brk(self):
        print("swift have brak")


class Innova:
    def start(self):
        print("innova car start method")

    def accelerate(self):
        print("innova can accelerate")

    def brk(self):
        print("innova have brak")

class Person:
    def drive(self,car):
       # self.car=car
       car.start()
       car.accelerate()
       car.brk()

sw=Swift()
ino=Innova()
p=Person()
p.drive(ino)
