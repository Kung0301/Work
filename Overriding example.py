class Animal() :
    def eat(self):
       print("Eating Eating")
class Cat(Animal) :
    __name= ""
    def setName(self,text):
        self.name = text
        print("Setting new cat name =", self.name)
    def eat(self):
       print("Meoww", self.name)
cat1 = Cat()
cat1.name = "TT"
print(cat1.__name)
cat1.eat()