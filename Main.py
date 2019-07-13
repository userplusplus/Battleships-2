#Main
#Author: Dominic Martindale
#Date: 7/06/2019
#About: the runtime of the game

from Command import Command
from Gameboard import Gameboard
from Position import Position
from Ship import Ship
from Environment import Environment

#Setup
e = Environment()
print("Welcome to battleships, the incomplete game!." +
      "\nTo place a ship type: \"place (orientation(v or h), x co-ord, y co-ord.\"" +
      "\nTo show the ships type: \"show battleships\"" +
      "\nTo exit the game type: \"exit battleships\"")

#Game loop
while True:
    e.process_command()
    if e.command.command_type == "exit"\
        and e.command.command_data == "battleships":
        print("\n\nThanks for playing!")
        break
    e.map_output()
