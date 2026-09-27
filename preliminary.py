class Car:
    def __init__(self, color, speed = 0) :
        self.color = color
        self.speed = speed
    def speedUp(self) : self.speed += 10
    def speedDown(self) : self.speed -= 10
    def __eq__(self, carB) : return self.color == carB.color
    def __str__(self):
        return "color = %s, speed = %d" % (self.color, self.speed)

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True) :
        super().__init__(color, speed)
        self.bTurbo = bTurbo
    def setTurbo(self, bTurbo = True) :
        self.bTurbo = bTurbo
    def speedUp(self):
        if self.bTurbo :
            self.speed += 50
        else :
            super().speedUp()
    def __str__(self):
        if self.bTurbo :
            return "[%s] [speed = %d] 터보모드" % (self.color, self.speed)
        else :
            return "[%s] [speed = %d] 일반모드" % (self.color, self.speed)

car1 = Car('black', 0)
car2 = Car('red', 120)
car3 = Car('yellow', 30)
car4 = Car('blue', 0)
car5 = Car('green')

car3.color = 'purple'
car5.speed = 100

s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White", 0, False)

s1.speedUp()
s2.speedUp()
print("슈퍼카1:",s1)
print("슈퍼카2:",s2)

print("\n===== Car 속성 확인 =====")
print("car1 → color:", car1.color, "speed:", car1.speed)
print("car2 → color:", car2.color, "speed:", car2.speed)
print("car3 → color:", car3.color, "speed:", car3.speed)
print("car4 → color:", car4.color, "speed:", car4.speed)
print("car5 → color:", car5.color, "speed:", car5.speed)

print("\n===== SuperCar 속성 확인 =====")
print("s1 → color:", s1.color, "speed:", s1.speed, "bTurbo:", s1.bTurbo)
print("s2 → color:", s2.color, "speed:", s2.speed, "bTurbo:", s2.bTurbo)