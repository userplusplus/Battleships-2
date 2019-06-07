#Commands
# Author: Dominic Martindale
# Note: Mostly pulled from iQualify
# Date: 6/06/2019
# About: parses player input into and checks against existing commands

class Command:
    def __init__(self):
        # here are some initialised variables
        self.__command_type = str
        self.__is_successful = False
        self.__error_message = "The command you entered was not recognised."
 
    @property # getter
    def command_type(self):
        return self.__command_type
 
    @command_type.setter
    def command_type(self, value):
        self.__command_type = value
 
    @property # getter
    def is_successful(self):
        return self.__is_successful
 
    @is_successful.setter
    def is_successful(self, value):
        self.__is_successful = value
 
    @property # getter
    def error_message(self):
        return self.__error_message
 
    # get the command, check it and set the property
    def get_user_command(self):
 
        # Important! set flag to false here too, in case it is true from a previous user entry
        self.is_successful = False
 
        user_input = input("\nEnter your command: ").split(" ")
 
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
