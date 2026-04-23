from creature import Creature
from creature import Pred
from grid import Grid

map = Grid(10,10)
map.add(Pred((2,2)))
map.add(Creature((5,5)))
map.add(Creature((0,0)))



def update(grid) -> None:
    """
    updates the map by giving:
        grid: grid object to update
    
    returns None"""
    #buffer 
    buffer_lst = []
    for row in grid.grid:
        for el in row:
            if el != 0:
                 near_food = grid.get_nearest(el.position, grid.get_foods())
                 near_preds = grid.get_nearest(el.position, grid.get_preds())
                 near_creatures = grid.get_nearest(el.position, grid.get_creatures())
                 buffer_lst.append((el.final_coord(el.get_delta_pos(near_food, near_preds, near_creatures), grid.l, grid.h), el.position))
    
    for action in buffer_lst:
        or_position = action[1]
        final_pos = action[0]
        obj = grid.grid[or_position[1]][or_position[0]]

        if obj.role:
            to_eat = obj.eat(grid.grid)
            if to_eat is not None:
                grid.grid[to_eat[1]][to_eat[0]] = 0
        grid.move_obj(or_position, final_pos)




for _ in range(20):
    print(map)
    update(map)
    
