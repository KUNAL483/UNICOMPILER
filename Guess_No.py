

import random


x=int(input("Enter the starting range "))
y=int(input("Enter the ending range "))
secret_number = random.randint(x,y)

def prime(secret_number):
    flag=False
    if secret_number == 1:
        print("The number is not prime ")
    elif secret_number > 1:
        for i in range (2,secret_number):
            if secret_number%i==0:
                flag=True
                break
    if flag:
        print("The Secret number is not prime ")
    else:
        print("The Secret number is prime ")



def odd_even(secret_number):
    if secret_number%2==0:
        print("The Number is Even")
    else:
        print("The Number is odd")




def guess():
    print(secret_number)
    print ("--------Welcome To the Number Guessing Game -----")
    print ("-----RULES---")
    print ("You'll be given 5 chances to guess the secret number .....Good Luck")
    print("")
    guessed=0
    
    guessed=int(input("1. Guess the secret number "))
    if guessed==secret_number:
        print(f"Congratulations  you guessed it right . The secret number was {secret_number}")
        
    elif guessed!=secret_number:
        print("HINTS")
        prime(secret_number)
        odd_even(secret_number)
        print("")
    if guessed!=secret_number:
        c=2
        for i in range (0,4):
            print("")
            guessed=int(input(f"{c}. Guess the secret number "))
            c+=1
            if guessed>secret_number:
                print ("Sorry you guessed too high ")
            elif guessed<secret_number:
                print ("Sorry the number you guessed is too low")
            elif guessed==secret_number:
                print (f"Congratulations  you guessed it right . The secret number was {secret_number}")
            
        if guessed!=secret_number:
            print("")
            print(f"Sorry No more Chances...The secret number was {secret_number}")

guess()
