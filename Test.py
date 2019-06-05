from Position import Position
from Gameboard import Gameboard
from Ship import Ship

#p = Position(1,1)
#p1 = Position(5,5)

#How to compare 2 positions
#print(p1.x == p.x and p1.y == p.y)


g = Gameboard(5,5)

#g.is_valid_position(p1)

#g.update_position(p1, True)

ship = Ship("h",1,1)

ship.place_ship(g)
ship.show_positions()
print(ship.all_positions[0].x)
print(ship.all_positions[1].x)
print(ship.all_positions[2].x)
