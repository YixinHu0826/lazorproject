'''
This is the main code that solves any given board in .bff file
'''
# this is a test
def shoot_laser(grid, lasers):
    '''
    Shoot laser through the completed grid with blocks, and
    retain all the points that the laser passes through
    '''
    passed_points = []

    def laser_step(laser, grid):
        # acquire current position and direction
        curr_pos = laser.get_position()
        curr_dir = laser.get_direction()
        # check if the current position is out of bounds
        if check(curr_pos, grid) is False:
            return
        # Identify block of interest

        def find_row_col (curr_pos, curr_dir):
            if curr_pos[0] % 2 == 0: # if x coordinate is even
                if curr_dir[0] == 1:
                    row_num = int((curr_pos[1]-1)/2)
                    col_num = int(curr_pos[0]/2)
                else:
                    row_num = int((curr_pos[1]-1)/2)
                    col_num = int((curr_pos[0]-2)/2)
            else:
                if curr_dir[1] == 1:
                    row_num = int(curr_pos[1]/2)
                    col_num = int((curr_pos[0]-1)/2)
                else:
                    row_num = int((curr_pos[1]-2)/2)
                    col_num = int((curr_pos[0]-1)/2)
            return row_num, col_num
        row_num, col_num = find_row_col(curr_pos, curr_dir)
        # check if interested block is out of bounds
        if row_num < 0 or col_num < 0:
            return
        # check if interested block is out of bounds
        if row_num >= len (grid) or col_num >= len (grid[0]):
            return
        interested_block = grid[row_num][col_num]
        # Identify what type of block is encountered
        if interested_block == 'A': # reflect
            if curr_pos[0] % 2 == 0:
                laser.change_direction((curr_dir[0]*(-1),curr_dir[1])) # flip x only
            else:
                laser.change_direction((curr_dir[0],curr_dir[1]*(-1))) # flip y only
            # Need to account for the case where the starting points are both reflect blocks, 
            # for which this code will keep recursively calling itself
            new_dir = laser.get_direction()
            temp_row_num, temp_col_num = find_row_col(curr_pos,new_dir)
            if temp_row_num < 0 or temp_col_num < 0:
                return
            if temp_row_num >= len (grid) or temp_col_num >= len (grid[0]):
                return
            new_block = grid[temp_row_num][temp_col_num]
            if new_block == 'A':
                return
            laser_step(laser, grid)
        elif interested_block == 'B': # opaque, ray operation ends here
            return
        elif interested_block == 'C': # refract
            new_pos = (curr_pos[0]+curr_dir[0], curr_pos[1]+curr_dir[1])
            if new_pos not in passed_points:
                passed_points.append(new_pos)
            new_laser = Laser(new_pos,curr_dir)
            laser_step(new_laser, grid)
            if curr_pos[0] % 2 == 0:
                laser.change_direction((curr_dir[0]*(-1),curr_dir[1]))
            else:
                laser.change_direction((curr_dir[0],curr_dir[1]*(-1)))
            # Need to account for the case where the starting points are both reflect blocks, 
            # for which this code will keep recursively calling itself
            new_dir = laser.get_direction()
            temp_row_num, temp_col_num = find_row_col(curr_pos,new_dir)
            if temp_row_num < 0 or temp_col_num < 0:
                return
            if temp_row_num >= len (grid) or temp_col_num >= len (grid[0]):
                return
            new_block = grid[temp_row_num][temp_col_num]
            if new_block == 'A':
                return
            laser_step(laser, grid)
        else:
            new_pos = (curr_pos[0]+curr_dir[0], curr_pos[1]+curr_dir[1])
            if new_pos not in passed_points:
                passed_points.append(new_pos)
            laser.change_position(new_pos)
            laser_step(laser, grid)

    for laser in lasers:
        temp_pos = laser.get_position()
        temp_dir = laser.get_direction()
        temp_laser = Laser(temp_pos,temp_dir)
        laser_step(temp_laser, grid)
    return passed_points

def check(curr_pos, grid):
    '''
    Check if a given point is out of bounds
    '''
    rows = len(grid)*2
    cols = len(grid[0])*2
    if curr_pos[1]>rows or curr_pos[0]>cols:
        return False
    if curr_pos[1]<0 or curr_pos[0]<0:
        return False
    return True

def check_solution(passed_points, required_points):
    '''
    Check if the current solution contains all points required
    '''
    for point in required_points:
        if point not in passed_points:
            return False
    return True

def initialize_board (org_grid, available_slots, perm):
    '''
    Put value of permutation onto original board
    '''
    new_grid = org_grid
    for i, slot in enumerate(available_slots):
        new_grid [slot[0]][slot[1]] = perm [i]
    return new_grid

if __name__ == "__main__":
    pass