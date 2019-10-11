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

    def __init__(self):
        self.dice_sides = 0
        self.roll_count = 0
        self.roll_list = []
    
    def number_of_sides(self):
        sides = input("How many sides does your dice have? " )
        while not sides.isdigit():
            print("This is not a number")
            self.number_of_sides()
        else:
            self.dice_sides = sides
            print("Your dice this round will have " + self.dice_sides + " sides")
            
        self.number_of_rolls()
        
    def number_of_rolls(self):
        
        rolls = input("How many rolls will you do this round? ")
        while not rolls.isdigit():
            print("This is not a number")
            return self.number_of_rolls()
        else:
            self.roll_count = int(rolls)
            print("This round will have " + str(self.roll_count) + " rolls")
            print(self.roll_count)
        self.add_roll_count()

    def add_roll_count(self):
        print(self.roll_count)
        starting_roll_count = 0
        
        while starting_roll_count < self.roll_count:
            random_roll = random.randint(1, int(self.dice_sides))
            self.roll_list.append(random_roll)
            starting_roll_count = starting_roll_count + 1
        print(self.roll_list)
        for number in self.roll_list:
            count = self.roll_list.count(number)
            # if item in number:
            #     print(item)
            print(count)
            # print("x showed up x times" + str(count))
        # self.add_roll_count
    
 
        
               
            
           
    
#have the user choose a number for side of die.
#have the user choose how many times you want to roll the die.
#throw the die x amount of times, for each roll return a random number between 1 and the number of sides.
#save the random number and roll # to a list that gets printed every loop
       
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





