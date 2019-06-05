#Gameboard
#Author: Dominic Martindale
#Date 6/06/2019
#About: A class which creates a grid based game
#       board in which ships can be placed onto.

from Position import Position

#Acts as a container for the game data which can be updated with new data.
class Gameboard:
 
    # constructor does setting
    def __init__(self, x_size, y_size, all_positions=None):
        self.__x = x_size
        self.__y = y_size

        #If all_postions is not specified, the gameboard will
        # create 25 instances of the position obj
        if all_positions == None:
            self.__all_positions = self.create_positions()
        else:
            self,__all_positions = all_positions

    @property # getter
    def x(self):
        return self.__x
 
    @property # getter
    def y(self):
        return self.__y
    # x and y setters in constructor

    @property #getter
    def all_positions(self):
        return self.__all_positions

    #Create positions based off of x and y (automated setter)
    def create_positions(self):
        x_counter = 1
        y_counter = 1
        my_list = []
        #for how many units in y (column)
        for x in range(int(self.y)):
            #for how many units in x (row)
            for x in range(int(self.x)):
                #Create a position, then append it and increment x
                new_pos = Position(x_counter, y_counter)
                my_list.append(new_pos)
                x_counter += 1
            #When x loop has finished row, increment column and reset x
            x_counter = 1
            y_counter += 1
        #Return all positions
        return my_list

    #update positon's is_occupied value to specified bool
    def update_position(self, check_position, input_bool):
        p = check_position
        n = 0 #counter

        #check for correct input of bool, continue if fine
        if type(input_bool) == bool:
            for x in self.all_positions:
                #Compares x and y values of check-pos against current co-ord in list
                if p.y == self.all_positions[n].y and p.x == self.all_positions[n].x:
                    #Change match to new boolean
                    self.all_positions[n].is_occupied = input_bool
                    break
                n +=1
            else:
                #Iterated through whole list and found no matches
                print("Your input did not match to any positions on the gameboard") #error
        else:
            #bool not bool input
            print("The boolean argument was not a boolean value type.") #error

    #Checks to see if the position is taken in the gameboard
    #Returns 0 if taken, 1 if not taken.
    #Also returns 0 if co-ords are non-existant on the gameboard.
    def is_valid_position(self, check_position):
        p = check_position
        n = 0 #counter
        
        for x in self.all_positions:
            #Un-comment to show test log loop
            print("Currently testing: ("+ str(p.x) + "," + str(p.y) + ") against ("+
            str(self.all_positions[n].x) + "," + str(self.all_positions[n].y) + ")")
            
            #Compares x and y values of check-pos against current co-ord in list
            if p.y == self.all_positions[n].y and p.x == self.all_positions[n].x:
                if self.all_positions[n].is_occupied == True:
                    print()
                    return False
                else:
                    #Co-ords are a match to existing one on gameboard
                    #and it isnt occupied - valid position
                    return True
            n += 1
            
        else:
            #Iterated through whole list and found no matches
            print("Your input did not match to any positions on the gameboard") #error
            return False
