from currency_converter import CurrencyConverter
c = CurrencyConverter()
print("นี่คือโปรแกรมเปรียบเทียบสกุลเงิน")
print("โปรดใส่จำนวนเงิน")
value = float(input())
def exchange() :
    print("โปรดเลือกสกุลเงิน :")
    print("USD")
    print("CNY")
    print("JPY")
    print("SGD")
    print("GBP")
    choose = input("สกุลเงินที่เลือก :")
    if choose == "USD" :
        print(c.convert(value,'THB','USD'), "USD")
    elif choose == "CNY" :
        print(c.convert(value,'THB','CNY'), "CNY")
    elif choose == "JPY" :
        print(c.convert(value,'THB','JPY'), "JPY")
    elif choose == "SGD" :
        print(c.convert(value,'THB', 'SGD'), "SGD")
    elif choose == "GBP" :
        print(c.convert(value,'THB','GBP'), "GBP")
    else :
        print("โปรดทำรายการอีกครั้ง")
        return exchange()
exchange()
print("ทำรายการเสร็จสิ้น")