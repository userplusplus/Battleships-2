#Position
#Author : Dominic Martindale
#Date: 6/06/2019
#About: A constructor for creating an container object with x and y co-ords

class Position:

    #Sets x and y values.
    #Wether postion is occupied or not can be left blank
    # the default is not occupied.
    def __init__(self, x, y, is_occupied=None):
        self.__x = x
        self.__y = y

        #Allows is_occupied to have no initial value
        if is_occupied == None:
            self.__is_occupied = False #default value, if none given
        else:
            self.__is_occupied = is_occupied

    @property #Getter for x
    def x(self):
        return self.__x
 
    @x.setter #Setter for x, int only
    def x(self, value):
        if type(value) == int: #int checker
            self.__x = value
        else:
            return print("A wrong x value was entered into a position") #error
 
    @property #Getter for y
    def y(self):
        return self.__y
 
    @y.setter  #Setter for y int only
    def y(self, value):
        if type(value) == int: #int checker
            self.__y = value
        else:
            return print("A wrong x value was entered into a position") #error

    @property #Getter for is_occupied
    def is_occupied(self):
        return self.__is_occupied
 
    @is_occupied.setter  #Setter for is_occupied, boolean only
    def is_occupied(self, value):
        if type(value) == bool:  #boolean checker
            self.__is_occupied = value
        else:
            return print("A wrong is_occupied value was entered into a position") #error
