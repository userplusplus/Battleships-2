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
        self.__ship_total = 0 #counter for number of ships

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

    # output the all ship co-ords
    #def get_report(self):
        #for how many ships there are, output co-ords
        #for x in range(len(self.ship_list)):
         #   pass
            
 
    def process_command(self):
        # get the user command
        self.command.get_user_command()
 
        # check the is_successful property
        if self.command.is_successful:

            #Place command
            if self.command.command_type == "place":
                #If position chosen is valid
                if self.game_board.is_valid_position:
                    #Parse user string data from user_input
                    # expected input example: "v,1,1"
                    p = self.command.command_data.split(",")
                    #check for valid input, 3 parts, part 2 and 3 have a number aka co-ord
                    if len(p) < 3 and any(char.isdigit() for char in p[2])\
                       and any(char.isdigit() for char in p[3]):
                        #Create a ship in ship list
                        self.ship_list[self.ship_total] = Ship(p[0],p[1],p[2])
                    #use place command on ship
                    self.ship_list[self.ship_total].place_ship
                else:
                    print("Sorry, either that co-ord doesn't exist or is taken")

            #Show command
            elif self.command.command_type == "show":
                if self.toy_board.is_valid_position(self.toy_robot.get_down()):
                    self.toy_robot.robot_position = self.toy_robot.get_down()
            else:
                # the command must be exit
                if self.command.command_type == "report":
                    self.get_report()
                # don't need else here, 'exit' is implemented in main class
                # so that it breaks out of permanent loop
        else:
            print(self.command.error_message)
