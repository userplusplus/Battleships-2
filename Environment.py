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
        self.__ship = Ship()

    @property #Getter for gameboard, setter in constructor
    def game_board(self):
        return self.__game_board

    @property #Getter for command, setter in constructor
    def command(self):
        return self.__command

    @property #Getter for ship
    def ship(self):
        return self.__ship

    @ship.setter(self, details): #setter for ship
        return self.__ship(details)
