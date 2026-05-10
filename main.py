from creature import Creature
from creature import Pred
from grid import Grid
from food import Food
import os
import time
import random

def update(grid) -> None:
    """
    updates the map by giving:
        grid: grid object to update
    
    returns None"""
    #buffer 
    buffer_lst = []
    for row in grid.grid:
        for el in row:
            if el != 0 and not isinstance(el, Food):
                 near_food = grid.get_nearest(el.position, grid.get_foods())
                 near_preds = grid.get_nearest(el.position, grid.get_preds())
                 near_creatures = grid.get_nearest(el.position, grid.get_creatures())
                 buffer_lst.append((el.final_coord(el.get_delta_pos(near_food, near_preds, near_creatures), grid.l, grid.h), el.position))
    
    for action in buffer_lst:
        or_position = action[1]
        final_pos = action[0]
        obj = grid.grid[or_position[1]][or_position[0]]

        if obj != 0:
            if obj.role:
                to_eat = obj.eat(grid.grid)
                if to_eat is not None:
                    grid.grid[to_eat[1]][to_eat[0]] = 0
            grid.move_obj(or_position, final_pos)

def random_add(num_of_preds: int, num_of_creat : int, num_of_food: int, grid: Grid, food_h=30):
    free_spaces = grid.get_spaces()
    if (num_of_creat + num_of_preds + num_of_food) > len(free_spaces):
        return 
    
    for counter, to_add in enumerate((num_of_preds, num_of_creat, num_of_food)):
        for i in range(to_add):
            coord = free_spaces[(indx := random.randrange(len(free_spaces)))]
            del free_spaces[indx]
            match counter:
                case 0:
                    grid.add(Pred(coord))
                case 1:
                    grid.add(Creature(coord))
                case 2:
                    grid.add(Food(coord, food_h))


l = 30
mapp = Grid(l,l)
random_add(0, 10, 70, mapp)


while True:
    print(mapp)
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    update(mapp)
    
