class Customer :
    name = ""
    lastname = ""
    age = 0
    def addCart(self) :
        print("Add to ", self.name, self.lastname+"'s cart")

customer1 = Customer()
customer1.name = "Pat"
customer1.lastname = "Tum"
customer1.addCart()