from random import shuffle
 # The game
def the_game():
    """""
    1. The computer will think of 3 digit number that has no repeating digits.
2. You will then guess a 3 digit number
3. The computer will then give back clues, the possible clues are:
 Close: You've guessed a correct number but in the wrong position
 Match: You've guessed a correct number in the correct position
 Nope: You haven't guess any of the numbers correctly
4. Based on these clues you will guess again until you break the code with a
 perfect match!
    """""
    print('Welcome stranger, guess the  3 digit number')
    the_number =  list(range(1, 10))
    shuffle(the_number)
    the_number = the_number[:3]
    guess = 0
    print(f'{the_number} - here is the correct unswer for debug') #for debug
    sucsess = False
    while not sucsess:
        try:
            guess = int(input("What is your guess? \n For quit type -1\n"))
        except:
             print("Please, write the number next time, not some text")
        if guess == -1: 
            print('Goodbye stranger')
            return
             

        print(f'guess = {guess}')
        print(f'the_number = {the_number[0]*100+the_number[1]*10+the_number[2]} - here is the correct unswer for debug')
        print(guess == the_number[0]*100+the_number[1]*10+the_number[2])
        if guess == the_number[0]*100+the_number[1]*10+the_number[2]:
            print("Match: You've guessed a correct number in the correct position")
            sucsess = True
            return
        if guess % 10 in the_number or guess//100 in the_number or guess % 100 %10 in the_number:
            print("Close: You've guessed a correct number but in the wrong position")
        else:
            print("Nope: You haven't guess any of the numbers correctly")

