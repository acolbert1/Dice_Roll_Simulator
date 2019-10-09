#allow the user to input any number of sides, and how many times it needs to be rolled.
#when the user rolls the dice, keep track of the number that shows up. i.e. if the user rolls a dice and the number is 4, keep track of the number of times 4 shows up.
#print out how many times each number shows up. 
#. if the user does not type in a number when prompted, the program will keep prompting them for a digit.
#put the program in a loop so that the user can keep going and have the option to quit.
#.In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.

#bonus.  1. Create a program that opens a new window and draws 2 six-sided dice
#2. Allow the user to quit, or roll again
#Allow the user to select the number of dice to be drawn on screen(1-4) 2. Add up the total of the dice and display it

import random

class dice_role_simulator:
    
    def number_of_sides(self):
        sides = input("How many sides does your dice have? " )

        while not sides.isdigit():
            print("This is not a number")
            return self.number_of_sides()
        else:
            print("Your dice this round will have " + sides + " sides")
            
        self.number_of_rolls()

        
    def number_of_rolls(self):
        rolls = input("How many rolls will you do this round? ")
        

        while not rolls.isdigit():
            print("This is not a number")
            return self.number_of_rolls()
        else:
            print("This round will have " + rolls + " rolls")
            rolls = int(rolls)
            random_roll = str(random.randint(1, rolls))
            print(random_roll)
            
            
    

       
    #randomint between 1 and the number of sides
    
       
        # # if not user_input.isdigit():
        # #     print("This is not a number please enter a number")
        # #     return self.dice_roll() 
        # # else:
        # #     print("Your dice this round will have " + user_input + " sides")
            
        
        # while not number_of_sides.isdigit():
        #     print("This is not a number")
        #     return self.dice_roll()

        # if number_of_sides.isdigit():
        #     print("Your dice this round will have " + number_of_sides + " sides")
            
        # while not number_of_sides.isdigit():
        #     print("This is not a number")
        #     return self.dice_roll()


dice_roll_game = dice_role_simulator()
dice_roll_game.number_of_sides()





