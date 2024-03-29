#Ship
#Author: Dominic Martindale
#Date: 6/06/2019
#About: Contains the ship constructor that all ships are based off of.

from Position import Position

class Ship:

    def __init__(self, orientation, x, y, length=None, all_positions=None):
        #The orientation, v for vertical, h for horizontal.
        self.__orientation = orientation

        #The x and y co-ords that the initial placement of the ship is based off of
        self.__x = int(x)
        self.__y = int(y)

        #The length of the ship in units.
        if length == None:
            self.__length = 3 #default value
        else:
            self.__length = length

        #All 'positions' of the ship, 3 total
        if all_positions == None:
            self.__all_positions = []
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

    @property #Getter for length
    def length(self):
        return self.__length
    
    @property #Getter for all_positions
    def all_positions(self):
        return self.__all_positions
    
    @all_positions.setter #Setter for all_positions
    def all_positions(self, value):
        self.__all_positions = value

    #Set all positions of the ship, checking them one
    # at a time then save them as __all_positions.
    #If any check fail, delete obj instance and print accordingly
    def place_ship(self, gameboard):
        g = gameboard
        curr_x = self.x
        curr_y = self.y
        all_pos = []

        for i in range(int(self.length)):
            #Create new object for array entry so they are all unique
            p = Position(curr_x, curr_y)
            
            #If the position exists on the gameboard and not taken (is_occupied)
            if g.is_valid_position(p):
                #append to co-ords to temporary
                all_pos.append(p)
                #update checked axis position by 1 depending on orientation
                if self.orientation == "h":
                    #horizontal
                    curr_x += 1
                else:
                    #vertical
                    curr_y += 1
            else:
                #A co-ord that was checked is invalid
                return False
        
        #Set position on gameboard to occupied for each position
        n = 0
        for x in all_pos:
            g.update_position(all_pos[n], True)
            n += 1

        #assign all positions to the ship
        self.all_positions = all_pos
        return True

    #output all_positions
    def show_positions(self):
        string = "Ship at: "
        n = 0 #counter
        for x in self.all_positions:
            #append co-ord as string to string to print for each co-ord existing
            string += "(" + str(self.all_positions[n].x) + "," + str(self.all_positions[n].y) + ") "
            n += 1
        return string
