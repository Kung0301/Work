def vat_cal() :
    x = int(input())
    result = x+(x*7/100)
    return int(result)

print(vat_cal())