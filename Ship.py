#Ship
#Author: Dominic Martindale
#Date: 6/06/2019
#About: Contains the ship constructor that all ships are based off of.


class Ship:

    def __init__(self, orientation, x, y, length=None, all_positions=None):
        #The orientation, v for vertical, h for horizontal.
        self.__orientation = orientation

        #The x and y co-ords that the initial placement of the ship is based off of
        self.__x = x
        self.__y = y

        #The initial co-ords of the ship.
        self.__position = Position(self.x, self.y)

        #The length of the ship in units.
        if length == None:
            self.__length = 3 #default value
        else:
            self.__length = length

        #All 'positions' of the ship, 3 total
        if all_positions == None:
            self.__all_positions = self.place_ship()
        else:
            self.__all_positions = all_positions
        

    @property #Getter for orientation
    def orientation(self):
        return self.__orientation

    @property #Getter for x
    def x(self):
        return self.__x

    @property #Getter for y
    def y(self):
        return self.__y

    @property #Getter for position
    def position(self):
        return self.__position

    @property #Getter for length
    def length(self):
        return self.__length
    
    @property #Getter for all_positions
    def length(self):
        return self.__all_positions

    #Set all positions of the ship, save them as __all_positions
    def place_ship(self, gameboard):
        p = self.position
        g = gameboard
        n = 0 #counter
        #check orientation
        if self.orientation == "h":
            #horizontal
            for x in range(self.length):
                
                g.is_valid_position(p)

        if self.orientation == "v":
            #vertical
            for x in self.length
