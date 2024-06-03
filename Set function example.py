user_input = int(input("Enter number of fruits you like :"))
my_fruits = set()
while (len(my_fruits)<user_input) :
    my_fruits.add(input("Fruits :"))
    print(my_fruits)