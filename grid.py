from math import sqrt
from creature import Creature
from creature import Pred
from food import Food

class Grid:
    def __init__(self, l: int, h: int):
        self.grid: list[list] = [[0]*l for _ in range(h)]
        self.l = l
        self.h = h
    def __str__(self):
        #replace 0 with ~
        printable_grd = [[i if i == 0 else '~' for i in self.grid[n]] for n in range(self.h)]
        #what is printed
        return "".join([str(printable_grd[i])+'\n' for i in range(self.h)])\
                .replace("[", "").replace("]", "")
    def add(self, to_add: Creature):
        """
        tries to replace pos with to_add if space is empty by giving:
            to_add: obj to add
        
        returns None"""
        pos = to_add.position
        if self.grid[pos[1]][pos[0]] == 0:
            self.grid[pos[1]][pos[0]] = to_add
    def move_obj(self, init_pos: tuple[int, int], final_pos: tuple[int, int]):
        """
        Tries to move an object to another position by giving:
            init_pos: initial position
            final_pos: final position
        returns None"""

        #check if it can move obj in init_pos
        if isinstance(self.grid[init_pos[1]][init_pos[0]], Creature) and self.grid[final_pos[1]][final_pos[0]] == 0:
            #final_pos = obj , init_pos = 0
            self.grid[final_pos[1]][final_pos[0]] = self.grid[init_pos[1]][init_pos[0]]
            self.grid[init_pos[1]][init_pos[0]] = 0
            self.grid[final_pos[1]][final_pos[0]].position = final_pos
    def get_preds(self):
        """
        gets coords of all predators on the grid
        """
        found = []
        for row in self.grid:
            for element in row:
                if isinstance(element, Pred):
                    found.append(element.position)
        return tuple(found)
    def get_creatures(self):
        """
        gets coords of all creatures on the grid
        """
        found = []
        for row in self.grid:
            for element in row:
                if type(element) == Creature:
                    found.append(element.position)
        return tuple(found) if found else None
    def get_foods(self):
        """
        gets coords of all food on the grid
        """
        found = []
        for row in self.grid:
            for element in row:
                if isinstance(element, Food):
                    found.append(element.position)
        return tuple(found) if found else None
    def get_nearest(self, obj_coord: tuple[int, int], coords: tuple[tuple[int, int]]):
        """
        Gets the nearest obj to an other object by giving:
            obj_coord: the reference point
            coords: the coords of all the objs that the method checks
            
        returns (x,y) where x,y in range(l), range(h)"""
        distances = []
        nearest = ()
        if not coords:
            return None
        set_coords = set(coords)
        set_coords.discard(obj_coord)
        for coord in set_coords:
            x = coord[0]
            y = coord[1]
            distance = sqrt((obj_coord[0]-x)**2 + (obj_coord[1]-y)**2)
            distances.append(distance)
            if min(distances) == distance:
                nearest = (x, y)
        return nearest if nearest else None

            
