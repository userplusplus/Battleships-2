#Commands
# Author: Dominic Martindale
# Note: Mostly pulled from iQualify
# Date: 6/06/2019
# About: parses player input into and checks against existing commands

class Command:
    def __init__(self):
        self.__command_type = str
        self.__command_data = str #updated after parsing user input but needs to be callable
        self.__is_successful = False
        self.__error_message = "The command you entered was not recognised."
 
    @property #Getter for command_type
    def command_type(self):
        return self.__command_type
 
    @command_type.setter #Setter for command_type
    def command_type(self, value):
        self.__command_type = value
 
    @property #Getter for is_successful
    def is_successful(self):
        return self.__is_successful
 
    @is_successful.setter #Setter for is_successful
    def is_successful(self, value):
        self.__is_successful = value
 
    @property #Getter for error_message
    def error_message(self):
        return self.__error_message

    @property #Getter for command_data
    def command_data(self):
        return self.__command_data

    @command_data.setter #Setter for command_data
    def command_data(self, value):
        self.__command_data = value
 
    # get the command, check it and set the property
    def get_user_command(self):
 
        # Important! set flag to false here too, in case it is true from a previous user entry
        self.is_successful = False

        user_input = input("\nEnter your command: ").split(" ")
        print(user_input)
        
        # if the command is not valid
        if user_input[0] != "show"\
            and user_input[0] != "exit" \
            and user_input[0] != "place":
            # do nothing here.... leave the is_successful as false
            pass
        # else set is_successful to true and set the command_type
        else:
            self.is_successful = True
            self.command_type = user_input[0]
            if user_input[1] != None:
                self.command_data = user_input[1]
