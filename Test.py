from Position import Position
from Gameboard import Gameboard

p = Position(1,1)
p1 = Position(5,5)

#How to compare 2 positions
print(p1.x == p.x and p1.y == p.y)


g = Gameboard(5,5)
print(str(g.x))
print(str(g.y))

#g.is_valid_position(p1)

g.update_position(p1, True)


