input_round = int(input("Please enter number"))
sum = 0
for x in range(input_round) :
    input_number = int(input("x"+str(x+1)+ " :"))
    sum = input_number + sum
print("Result", sum)