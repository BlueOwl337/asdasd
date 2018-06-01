#This code was written by WooJin Lee in Python 3.5.4 programming language
def state(): # function that returns the pet's current state, used to make the code much more readable and to prevent repetition of code everytime a state is needed
    if actual_weight > 0: #Checking if it isn't dead
        if actual_weight > ideal_weight / 2: # Checking if it is underweight
            if actual_weight < ideal_weight * 2: #Checking it is not overweight
                return 'Happy' #It will return the string 'Happy' if the IF statements were all True thus satisfying the conditions for a happy pet
            else:
                return 'Overweight' #It will return the string 'Overweight' if the actual weight is not is not under or equal to 0 or half of ideal weight but is over double the ideal
        else:
            return 'Underweight' #It will return the string 'Underweight' if the actual weight is not under or equal to 0 but is less than half of ideal
    else:
        return 'Dead' #It will return the string 'Dead' if the actual weight is under 0
    
def pet():
    global actual_weight #Declares the variable to be a global variable thus making it usuable in all functions defined
    global ideal_weight
    global name
    while True: #Loops the actions and variable originally present to keep the loop going was found to be useless and thus removed for efficiency.
        action = input('----------------------------------------------------------------\n[Current Weight:{}] [Ideal Weight:{}] [Current Status: {}]\nWhat would you like to do with {}?: [E | F | Q]'.format(actual_weight, ideal_weight, state(), name))
        #If the user inputted 'E' for exercise
        if action.upper().startswith('E'):
            if actual_weight >= 1:
                try:
                    time_exercised = int(action.upper().strip('E ')) #Fixed a bug where a lowercase e would not be detected due to action not being uppercase using upper() function here
                except:
                    print("-----------------------------------\n[Usage: 'E minutes' | E.g. 'E 20'] Only whole numbers can be entered as the time!")
                    pet() #This is to prevent a bug that would add the food value stored in the previous turn if the user entered an incorrect argument in the current turn
                if time_exercised >= 1 and time_exercised <= 200:
                    actual_weight -= time_exercised
                    print('-----------------------------------\n{} exercised very hard for {} minutes!'.format(name, time_exercised))
                else:
                    print('-----------------------------------\nYou must exercise atleast for a minute and for 200 minutes at most!')
            else:
                print("-----------------------------------\n{} is dead! You can press 'Q' to quit.".format(name))
        # If the user inputted 'F' to feed
        elif action.upper().startswith('F'):
            if actual_weight >= 1:
                try:
                    food = int(action.upper().strip('F ')) #'try' and 'except' used to catch any errors that might be caused by user inputting a non integer or float
                except:
                    print("-----------------------------------\n[Usage: 'F amount' | E.g. 'F 20'] Only whole numbers can be entered to feed the pet!")
                    pet() #This is to prevent a bug that would add the food value stored in the previous turn if the user entered an incorrect argument in the current turn
                if food >= 1 and food <= 200: #Checking if it is within limits defined by assesment
                    actual_weight += food
                    print('-----------------------------------\nYou gave {} {} grams of food!'.format(name, food))
                else:
                    print('-----------------------------------\nYou must feed atleast a gram of food and upto 200 grams at most!')
            else:

                print("-----------------------------------\n{} is dead! You can press 'Q' to quit.".format(name))
        # If the user inputted 'Q' to Quit
        elif action.upper() == 'Q':
            EXIT_LOOP = True #Variable is named with all capitals and seperated by a underscore to signify a use of a constant. (Constant since we do not change this variable)
            while EXIT_LOOP == True:
                if state() == 'Happy':
                    repeat = input(':-) | Your pet was happy! \nWould you like to play again? [Y | N]')
                elif state() == 'Dead':
                    repeat = input('R.I.P | {} has perished due to your lack of care. \nWould you like to play again? [Y | N] '.format(name)) 
                else:
                    repeat = input(':-( | Your pet was {} and sad. \nWould you like to play again? [Y | N]'.format(state()))
               #Checking If the answer to the question was 'Y', 'N' or invalid and then executing the correct response
                if repeat.upper() == 'Y':
                    start()
                elif repeat.upper() == 'N':
                    exit()
                else:
                    print("-------------------------------------------\nYou must enter either 'Y' or 'N'!") #Added the series of - to make the text more readable to the user, \n was used for new line instead of 2 prints for efficiency
        else:
            print('You must pick an option between F (Feed) | E (Exercise) | Q (Quit)!')


def start():
    global actual_weight
    global ideal_weight
    global name
    name = input("Hi! Welcome to your pet's home! First, let's name your pet. \n Please Enter your Pet's Name: ")
    print("{} is a great name for a pet! Now let's look after {}.\n--------------------------------".format(name, name))
    ideal_correct = False
    while ideal_correct == False:
        try:
            ideal_weight = int(input("Please enter your new pet's ideal weight in grams! (This will be what you aim your pet to be): "))
            if ideal_weight >= 1:
                ideal_correct = True
            else:
                print("A pet's ideal weight must atleast be 1!")
        except:
            print('--------------------------------\nYou can only enter whole numbers as weights!')
    actual_correct = False
    while actual_correct == False:
        try:
            actual_weight = int(input("Now please enter your pet's actual weight in grams!: "))
            if actual_weight >= 1:
                actual_correct = True
            else:
                print("A pet's actual weight must atleast be 1!")
        except:
            print('--------------------------------\nYou can only enter whole numbers as weights!')
    pet()
start()
