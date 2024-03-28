from random import shuffle
 # The game
def the_game():
    print('Welcome stranger, guess the  3 digit number')
    the_number =  list(range(1, 10))
    shuffle(the_number)
    the_number = the_number[:3]
    print(the_number) #for debug
    sucsess = False
    while not sucsess:
        guess = int(input("What is your guess? "))
        print(f'guess = {guess}')
        print(f'the_number = {the_number[0]*100+the_number[1]*10+the_number[2]}')
        print(guess == the_number[0]*100+the_number[1]*10+the_number[2])
        if guess == the_number[0]*100+the_number[1]*10+the_number[2]:
            print("Match: You've guessed a correct number in the correct position")
            sucsess = True
            return
        if guess % 10 in the_number or guess//100 in the_number or guess % 100 %10 in the_number:
            print("Close: You've guessed a correct number but in the wrong position")
        else:
            print("Nope: You haven't guess any of the numbers correctly")

        
        



    

the_game()