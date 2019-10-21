import random

class dice_role_simulator:

    def __init__(self):
        self.dice_sides = 0
        self.roll_count = 0
        self.roll_list = []
        self.my_dict = {}
    
    def number_of_sides(self):
        sides = input("How many sides does your dice have? ")
        while not sides.isdigit():
            print("This is not a number please try again.")
            self.number_of_sides()
        else:
            self.dice_sides = sides
            print("Your dice this round will have " + self.dice_sides + " sides. Let's continue.")
            
        self.number_of_rolls()
        
    def number_of_rolls(self):
        
        rolls = input("How many rolls will you play this round? ")
        while not rolls.isdigit():
            print("This is not a number please try again.")
            return self.number_of_rolls()
        else:
            self.roll_count = int(rolls)
            print("This round will have " + str(self.roll_count) + " rolls. Let's start!")
            
        self.add_roll_count()

    def add_roll_count(self):
        
        starting_roll_count = 0
        while starting_roll_count < self.roll_count:
            random_roll = random.randint(1, int(self.dice_sides))
            self.roll_list.append(random_roll)
            starting_roll_count = starting_roll_count + 1
        
        self.unique_numbers()

    def unique_numbers(self):
        
        for number in self.roll_list:
            if number in self.my_dict:
                self.my_dict[number] += 1
            
            if number not in self.my_dict:
                self.my_dict[number] = 1

        self.percentage()
       
    def percentage(self):

        dictionary_percentage = {}
      
        for number in self.my_dict:
            saved_value = round((self.my_dict.get(number)*100) / self.roll_count, 2)
            dictionary_percentage[number] = saved_value
        
        self.output(dictionary_percentage)

    def output(self, dictionary):   
         
        for key in dictionary:
            value = str(dictionary.get(key))
            print("This round the dice rolled a " + str(key) + ". " + "It appeared " + value + "% the time.")

        self.restart_roll()

    def restart_roll(self):
        restart_game = ""
        while restart_game != "n" and restart_game != "no" and restart_game != "yes" and restart_game != "y":
            restart_game = input("Would you like to play another round of dice roll? ")
            if restart_game == "yes" or restart_game == "y":
                print("Let's roll again!")
                self.dice_sides = 0
                self.roll_count = 0
                self.roll_list = []
                self.my_dict = {}
                self.number_of_sides()
            elif restart_game == "n" or restart_game == "no":
                print("Ending the game, see you next time.")
            
            else:
                print("That is not a correct input. Please input a yes or a no and try again.")
                
dice_roll_game = dice_role_simulator()
dice_roll_game.number_of_sides()

    

