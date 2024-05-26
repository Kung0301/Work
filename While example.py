correct_number = 15
user_guess = 0
while user_guess != correct_number :
    user_guess = int(input("Please guess :"))
    if user_guess > correct_number :
        print("Too large")
    elif user_guess < correct_number :
        print("Too small")
    elif user_guess == correct_number :
        print("Correct")