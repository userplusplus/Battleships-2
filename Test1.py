from Environment import Environment
from Command import Command

e = Environment()
e.process_command()

print(e.ship_list[0].show_positions())
