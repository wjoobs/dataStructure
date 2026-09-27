class Car:
    def __init__(self, color, speed = 0) :
        self.color = color
        self.speed = speed
    def speedUp(self) : self.speed += 10
    def speedDown(self) : self.speed -= 10
    def __eq__(self, carB) : return self.color == carB.color
    def __str__(self):
        return "color = %s, speed = %d" % (self.color, self.speed)

car1 = Car('black', 0)
car2 = Car('red', 120)
car3 = Car('yellow', 30)
car4 = Car('blue', 0)
car5 = Car('green')

car3.color = 'purple'
car5.speed = 100

print("car2==car6 : ", car2==car6)
print("car3==car6 : ", car3==car6)
print("[car3]", car3)