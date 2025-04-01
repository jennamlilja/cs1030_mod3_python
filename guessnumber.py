import random #importing random integers

number = random.randint(0,100) #the number will be between 0 and 100

print("Guess the magic number between 0 and 100") #shows what the user needs to enter in

guess = -1 #

while guess != number:
    guess = int(input("\nEnter your guess:")) #while the guess is not equal to the number, if the number is the same ass the guess, it'll tell you that it is correct
    if guess == number:
        print(f"Yes, the number is {number}")
    elif guess > number:
        print("Your guess is too high") #while the guess is higher than the number, it'll tell you that it's too high
    else:
        print("Your guess is too low") #otherwise, the number is too low, and it'll tell you that
