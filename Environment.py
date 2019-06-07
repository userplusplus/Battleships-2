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
        self.__ship_list = []

    @property #Getter for gameboard, setter in constructor
    def game_board(self):
        return self.__game_board

    @property #Getter for command, setter in constructor
    def command(self):
        return self.__command

    @property #Getter for ship
    def ship_list(self):
        return self.__ship_list

    # output the all ship co-ords
    #def get_report(self):
        #for how many ships there are, output co-ords
        #for x in range(len(self.ship_list)):
         #   pass
            
 
    def process_command(self):
        # get the user command
        self.command.get_user_command()
 
        # now check the is_successful property
        if self.command.is_successful:
            # use if elif to execute the appropriate methods
            if self.command.command_type == "place":
                if self.toy_board.is_valid_position(self.toy_robot.get_up()):
                    self.toy_robot.robot_position = self.toy_robot.get_up()
                else:
                    print("Sorry, either that co-ord doesn't exist or is taken")
            elif self.command.command_type == "down":
                if self.toy_board.is_valid_position(self.toy_robot.get_down()):
                    self.toy_robot.robot_position = self.toy_robot.get_down()
                else:
                    print("Ooops, not moved - get a bump instead!")
                    self.toy_robot.bumps += 1
            elif self.command.command_type == "left":
                if self.toy_board.is_valid_position(self.toy_robot.get_left()):
                    self.toy_robot.robot_position = self.toy_robot.get_left()
                else:
                    print("Ooops, not moved - get a bump instead!")
                    self.toy_robot.bumps += 1
            elif self.command.command_type == "right":
                if self.toy_board.is_valid_position(self.toy_robot.get_right()):
                    self.toy_robot.robot_position = self.toy_robot.get_right()
                else:
                    print("Ooops, not moved - get a bump instead!")
                    self.toy_robot.bumps += 1
            else:
                # the command must be exit or report
                if self.command.command_type == "report":
                    self.get_report()
                # don't need else here, 'exit' is implemented in main class
        else:
            print(self.command.error_message)
