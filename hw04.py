# ------------------------------------------------------
#        Name: (Thalia Borromeo)
#       Peers: (N/A)
#  References: (N/A)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    
    """ Read text from the user and then check if the conditions are met.
        if the secret word is inside the user text, print you used the secret word.
        if dog or Dog is inside the user text, print you used the word dog or Dog
        if anything else is submitted, print Try again."""
    
    while True:
        text = input("Give me a sentence: ")
        if secret_word in text:
            print("You used the secret word!")
            break
        elif "dog" in text or "Dog" in text:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break
        else:
            print("Try again")
    


# Task 2
def check_greater():
    """ The user will first bre prompted to enter two integers to compare them.
        if the first integer is greater than the second, print First is greater.
        if the second integer is greater than the first, print Second is greater.
        if the integers are equal, print try again and repeat the whole loop from the start."""
    
    while True:
        text1 = int(input("Give me your first integer: "))
        text2 = int(input("Give me your second integer: "))
        if text1 > text2:
            print("First is Greater!")
            print("Done")
            break
        elif text2 > text1:
            print("Second is Greater")
            print("Done")
            break
        else:
            print("Try again")



# Task 3
def get_special_numbers():
    """ Look at the range of numbers from 1 to 40.
        while going from 1 to 40,
        if the number is divisible by 2, skip it.
        if the number is not divisible by 3, skip it.
        if the number is divisible by 5, skip it.
        for the numbers that arent affected by those conditions, print them """
    for i in range(1,41):
        if i % 2 == 0:
            continue
        if i % 3 != 0:
            continue
        if i % 5 ==0:
            continue
        else:
            print(i)
        


# Task 4.a
def my_for_loop():
    """ The user inputs a string when prompted to give a string.
        the string will imediatly return if the string length is greater than or equal to 2 OR less than or equal to 5 OR includes a space.
        go through the string to check the following conditions:
        if the letter is a vowel, print {let} is a vowel
        if the letter is not a vowel, print {let} is a consonant"""
    text = input("Give me a string: ")
    
    if not (2 <= len(text) <= 5) or " " in text:
        print("bad word")
        return
    
    vowel = "aeiouAEIOU"
    
    for let in text:
        if let in vowel:
            print(f"{let} is a vowel")
        else:
            print(f"{let} is a consonant")

# Task 4.b
def my_while_loop():
    """ The user inputs one of the three choices prompted, a, b, or c.
        if the choice is a, skip everything and return to the choice prompt.
        if the choice is b, print Goodbye.
        if the choice is c, the program exits immediately.
        if any other letter is chosen, print try againpy"""
    while True:
        choice = input("Choose an option: a, b, c: ")
        
        if choice == "a":
            continue
        elif choice == "b":
            print("Goodbye")
            break
        elif choice == "c":
            sys.exit()
        else:
            print("try again")

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")
