system_menu = {"egg":10,"meat":20,"fruit":40}
menuList = []
def showBill():
    totalPrice = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    print("total price :",totalPrice)

while True:
    menuName = input("Plese Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,system_menu[menuName]])

showBill()