import random
from math import sqrt
from copy import deepcopy

class Creature:
    def __init__(self, position: tuple[int, int]):
        self.health = 100 #from 0-100
        self.hunger = 100 #from 0-100 is fine, <0 takes damage
        self.position = position #(x, y)
        self.role = ""
    def get_delta_pos(self, food_coord: tuple[int, int] | None, pred_coord:  tuple[int, int] | None, crture_coord: tuple[int, int] | None):
        """
        Gets the direction if the movement vector by giving:
            food_coord: nearest food source, None if not found
            pred_coord: neares predator, None if not found
            crture_coord: nearest normal creaturen, None if not found
            
        returns (x,y) where x,y in (-1,0,1)"""
        def helper(target) -> tuple[int, int]:
            dx_target = ((target[0] - self.position[0])// abs(target[0] - self.position[0])) if target[0] != self.position[0] else 0 #type: ignore
            dy_target = ((target[1] - self.position[1])// abs(target[1] - self.position[1])) if target[1] != self.position[1] else 0 #type: ignore
            return dx_target, dy_target
        #change here if you want to add more roles
        if not self.role:
            if food_coord is None and pred_coord is None:
                return random.randint(-1,1), random.randint(-1,1)
            elif food_coord is None:
                return tuple(-i for i in helper(pred_coord))
            elif pred_coord is None:
                return helper(food_coord)
            dist_from_pred = sqrt((self.position[0]-pred_coord[0])**2 + (self.position[1]-pred_coord[1])**2)
            dist_from_food = sqrt((self.position[0]-food_coord[0])**2 + (self.position[1]-food_coord[1])**2)

            if dist_from_pred <= dist_from_food:
                return tuple(-i for i in helper(pred_coord))
            return helper(food_coord)
        if crture_coord is None:
            return random.randint(-1,1), random.randint(-1,1)
        return helper(crture_coord)

    def final_coord(self, delta_pos: tuple[int, int], l, h):
        """
        Gets the final position after being given:
            delta_pos: from the method get_delta_pos
        
        returns (x, y) where x,y in range(l), range(h)"""
        #delta_pos = (x2-x1, y2-y1)
        x = self.position[0] + delta_pos[0]
        y = self.position[1] + delta_pos[1]
        final_coord = (max(0, min(l-1, x)), max(0, min(h-1, y)))
        return final_coord

class Pred(Creature):
    def __init__(self, position: tuple[int, int]):
        super().__init__(position)
        self.role = "Pred"

    def eat(self, grid):
        """
        Gets the creature coords that it can eat by giving:
            grid: grid object where it is currently located
            
        returns (x, y) where x,y in range(l), range(h) or None"""
        padded_grid = [(len(grid[0])+2)*[1]] + [[1] + i + [1] for i in deepcopy(grid) ] + [(len(grid[0])+2)*[1]]
        p = (self.position[0] + 1, self.position[1] + 1) #pos after padding
        to_check = ((p[0]-1, p[1]-1), (p[0], p[1]-1), (p[0]+1, p[1]-1), \
                    (p[0]-1, p[1]), (p[0]+1, p[1]), \
                    (p[0]-1, p[1] + 1), (p[0] , p[1] + 1), (p[0] + 1, p[1] + 1)) #checks after padding
        found = []

        for x, y in to_check:
            obj = padded_grid[y][x]
            if type(obj) == Creature: #preds dont eat preds
                found.append((obj.position[0], obj.position[1])) #pos before padding
        
        if found:
            self.health = min(100, self.health+10)
            return random.choice(found) #return creature to eat
    
        
