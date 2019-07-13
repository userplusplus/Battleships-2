#Environment
#Author: Dominic Martindale
#Date: 7/06/2019
#About: creates and calls instances of the other objects.

from Command import Command
from Gameboard import Gameboard
from Position import Position
from Ship import Ship

class Environment:
    def __init__(self):
        self.__game_board = Gameboard(5,5)
        self.__command = Command()
        self.__ship_list = [] #list of ship objects

    @property #Getter for gameboard, setter in constructor
    def game_board(self):
        return self.__game_board

    @property #Getter for command, setter in constructor
    def command(self):
        return self.__command

    @property #Getter for ship
    def ship_list(self):
        return self.__ship_list

    @ship_list.setter #Setter for ship_list
    def ship_list(self, value):
        self.__ship_list = value

    #Print the ouput of the map data
    def map_output(self):
        #Starts off with the top line of the game board.
        string =  "\n   BATTLESHIPS   " + "\n |1||2||3||4||5|"
        n = 0 #Counter for x
        n2 = 1 #Counter for y rows
        #for how many positions there are on the gameboard.
        for x in self.game_board.all_positions:
            #check for if you need a new line (once every 5)
            if n % 5 == 0:
                #have one line for the first line
                if n2 == 1:
                    string += "\n" + str(n2)
                    n2 += 1
                else:
                    string += "\n-\n" + str(n2)
                    n2 += 1
            #If there is a ship on the position, is boolean.
            if self.game_board.all_positions[n].is_occupied is True:
                string += " S "
            #if the position is empty
            else:
                string += " ~ "
            n += 1
        #then print the whole thing
        print(string)   
 
    def process_command(self):
        # get the user command
        self.command.get_user_command()
 
        # check the is_successful property
        if self.command.is_successful:
            #Place command
            if self.command.command_type == "place":
                #Parse user string data from user_input
                p = self.command.command_data.split(",")
                try:
                    pos = Position(int(p[1]),int(p[2]))
                    #Check Position
                    if self.game_board.is_valid_position(pos):          
                        #Continue if there are less than 2 ships
                        n = len(self.ship_list)
                        if n < 2:      
                            #check for valid input, 3 parts, part 2 and 3 have a number aka co-ord
                            try:
                                if len(p) < 3 and p[0] == "v" or "h" and any(char.isdigit() for char in p[1])\
                                    and any(char.isdigit() for char in p[2]):
                                    #Add a ship to the list
                                    self.ship_list.append(Ship(p[0],p[1],p[2]))
                                    #use place command on ship
                                    if self.ship_list[n].place_ship(self.game_board):
                                        if (self.ship_list[n].orientation == "h"):
                                            print("You have placed a ship horizontally. \n")
                                        else:
                                            print("You have placed a ship vertically. \n")
                            except:
                                print("Sorry, one of the co-ords either doesn't exist or is taken."\
                                      + "\nPlease try again.")
                        else:
                            print("Sorry you have reached the maximum number of ships.")
                except:
                    print("Sorry you have not entered a valid position.")

            #Show command
            elif self.command.command_type == "show":
                if self.command.command_data == "battleships":
                    if len(self.ship_list) > 0:
                        #First line of output
                        n = 0
                        string = "All of the co-ords for the ships:"
                        for x in self.ship_list:
                            string += "\n" + self.ship_list[n].show_positions()
                            n += 1
                            print(string)
                    else:
                        print("There are no ships to show!")
                
            else:
                # the command must be exit
                if self.command.command_type == "exit"\
                 and self.command.command_data == "battleships":
                    pass
                # don't need else here, 'exit' is implemented in main class
                # so that it breaks out of permanent loop
        else:
            pass
