#Ship
#Author: Dominic Martindale
#Date: 6/06/2019
#About: Contains the ship constructor that all ships are based off of.

from Position import Position

class Ship:

    def __init__(self, orientation, position, length=None):
        #The orientation, v for vertical, h for horizontal.
        self.__orientation = orientation

        #The initial co-ords of the ship.
        self.__position = position

        #The length of the ship in units.
        if length == None:
            self.__length = 3 #default value
        else:
            self.__length = length
        

    @property #Getter for orientation
    def orientation(self):
        return self.__orientation

    @property #Getter for position
    def position(self):
        return self.__position

    @property #Getter for length
    def length(self):
        return self.__length
