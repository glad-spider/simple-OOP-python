#тут описаны главные методы класса по умолчанию

class Dog(object):
    def __init__(self, name):
        self.name = name
        self.key = 0

    def getName(self):
        return self.name

class Cat(Dog):                         #передаем наследник
    def __init__(self, name, color):    #вызов конструктора
        super().__init__(name=name)     #вызов базового конструктора и передача параметров
        self.name = name
        self.color = color
    def getColor(self):
        return self.color

dog = Dog('Haski')                     #создание экземпляра класса
print(dog.getName())
cat = Cat(name=dog.getName(), color= 'red')
print(cat.getColor())                  #вызов базового метода




class Point():
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
        self.coordinations = (self.x, self.y)   #tuple

    #operator +
    def __add__(self, p):
        return Point(self.x+p.x,self.y+p.y)
    #operator -
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    #operator *
    def __mul__(self, p):
        return self.x * p.x, self.y * p.y
    #format ToString()
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'

    #точки на плоскости
    def __ge__(self, p):
        return self.length() > -p.length()
    def __gt__(self, p):
        return self.length() > p.length()
    def __le__(self, p):
        return self.length() < -p.length()
    def __lt__(self, p):
        return self.length() < p.length()

    #equals
    def __eq__(self, p):
        self.x == p.x and self.y == p.y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    def move_point(self, x, y):
        self.x+x
        self.y+y

p1 = Point(45,78)
p2 = Point(77,98)
print(p1, p2)
p3 = p1+p2
p4 = p1-p2
p5 = p3*p4
print(p3,p4, p5)
