from sympy.utilities.iterables import multiset_permutations
import unittest


# Define the basic classes first
class Blocks:
    """
    Represents the types of blocks available in the game.

    Attributes:
    - A_num (int): The number of reflect blocks (type A).
    - B_num (int): The number of opaque blocks (type B).
    - C_num (int): The number of refract blocks (type C).
    """

    def __init__(self, block_types):
        """
        Initializes the Blocks object with the given block types.

        Arguments:
        - block_types (list): List of block types ('A', 'B', 'C').

        Example:
        >> blocks = Blocks(['A', 'B', 'B', 'C', 'C', 'C'])
        >> blocks.A_num
        1
        >> blocks.B_num
        2
        >> blocks.C_num
        3
        """
        # Initialize counts for each block type
        self.A_num = 0
        self.B_num = 0
        self.C_num = 0

        # Count the occurrence of each block type in the given list
        for block in block_types:
            if block == 'A':
                self.A_num += 1
            elif block == 'B':
                self.B_num += 1
            else:
                self.C_num += 1

    def get_reflect(self):
        """
        Returns the number of reflect blocks (type A).

        Example:
        >> blocks = Blocks(['A', 'B', 'B', 'C', 'C', 'C'])
        >> blocks.get_reflect()
        1
        """
        return self.A_num

    def get_opaque(self):
        """
        Returns the number of opaque blocks (type B).

        Example:
        >> blocks = Blocks(['A', 'B', 'B', 'C', 'C', 'C'])
        >> blocks.get_opaque()
        2
        """
        return self.B_num

    def get_refract(self):
        """
        Returns the number of refract blocks (type C).

        Example:
        >> blocks = Blocks(['A', 'B', 'B', 'C', 'C', 'C'])
        >> blocks.get_refract()
        3
        """
        return self.C_num


class Laser:
    """
    Represents a laser in the game.

    Attributes:
    - position (tuple): The position of the laser as a tuple (x, y).
    - direction (tuple): The direction of the laser as a tuple (vx, vy).
    """

    def __init__(self, position, direction):
        """
        Initializes the Laser object with the given position and direction.

        Arguments:
        - position (tuple): The position of the laser as a tuple (x, y).
        - direction (tuple): The direction of the laser as a tuple (vx, vy).

        Example:
        >> laser = Laser((1, 2), (1, -1))
        >> laser.position
        (1, 2)
        >> laser.direction
        (1, -1)
        """
        self.position = position
        self.direction = direction

    def get_position(self):
        """
        Returns the current position of the laser.

        Example:
        >> laser = Laser((1, 2), (1, -1))
        >> laser.get_position()
        (1, 2)
        """
        return self.position

    def get_direction(self):
        """
        Returns the current direction of the laser.

        Example:
        >> laser = Laser((0, 0), (-1, 1))
        >> laser.get_direction()
        (-1, 1)
        """
        return self.direction

    def change_position(self, new_position):
        """
        Changes the position of the laser to the given position.

        Arguments:
        - new_position (tuple): The new position of the laser as tuple (x, y).

        Example:
        >> laser = Laser((1, 2), (1, -1))
        >> laser.change_position((3, 4))
        >> laser.get_position()
        (3, 4)
        """
        self.position = new_position

    def change_direction(self, new_direction):
        """
        Changes the direction of the laser to the given direction.

        Arguments:
        - new_direction (tuple): The new direction of
        the laser as tuple (vx, vy).

        Example:
        >> laser = Laser((0, 0), (-1, 1))
        >> laser.change_direction((1, 0))
        >> laser.get_direction()
        (1, 0)
        """
        self.direction = new_direction


class Game:
    """
    Represents a game instance.

    Attributes:
    - grid (list): The grid of the game.
    - blocks (Blocks): The available blocks in the game.
    - lasers (list): The lasers in the game.
    - points (list): The points that the lasers need to intersect.
    """

    def __init__(self, grid, blocks, lasers, points):
        """
        Initializes the Game object with the
        given grid, blocks, lasers, and points.

        Arguments:
        - grid (list): The grid of the game.
        - blocks (Blocks): The available blocks in the game.
        - lasers (list): The lasers in the game.
        - points (list): The points that the lasers need to intersect.

        Example:
        >> blocks = Blocks(['A', 'B', 'B', 'C', 'C', 'C'])
        >> lasers = [Laser((1, 2), (1, -1)), Laser((3, 4), (0, -1))]
        >> points = [(1, 1), (2, 2)]
        >> game = Game([[0, 'A', 0], ['B', 0, 'C']], blocks, lasers, points)
        >> game.grid
        [[0, 'A', 0], ['B', 0, 'C']]
        >> game.blocks
        <Blocks object at ...>
        >> game.lasers
        [<Laser object at ...>, <Laser object at ...>]
        >> game.points
        [(1, 1), (2, 2)]
        """
        self.grid = grid
        self.blocks = blocks
        self.lasers = lasers
        self.points = points

    def get_grid(self):
        """
        Returns the grid of the game.

        Example:
        >> game = Game([[0, 'A', 0], ['B', 0, 'C']], blocks, lasers, points)
        >> game.get_grid()
        [[0, 'A', 0], ['B', 0, 'C']]
        """
        return self.grid

    def get_blocks(self):
        """
        Returns the available blocks in the game.

        Example:
        >> game = Game([[0, 'A', 0], ['B', 0, 'C']], blocks, lasers, points)
        >> game.get_blocks()
        <Blocks object at ...>
        """
        return self.blocks

    def get_lasers(self):
        """
        Returns the lasers in the game.

        Example:
        >> game = Game([[0, 'A', 0], ['B', 0, 'C']], blocks, lasers, points)
        >> game.get_lasers()
        [<Laser object at ...>, <Laser object at ...>]
        """
        return self.lasers

    def get_points(self):
        """
        Returns the points that the lasers need to intersect.

        Example:
        >> game = Game([[0, 'A', 0], ['B', 0, 'C']], blocks, lasers, points)
        >> game.get_points()
        [(1, 1), (2, 2)]
        """
        return self.points


# Now we'll define the parser function to read
# from the .bff file and create a game instance
def parse_bff(file_path):
    """
    Parses a .bff file and creates a game instance.

    Arguments:
    - file_path (str): The path of the .bff file.

    Returns:
    - game (Game): The game instance created from the .bff file.

    Example:
    >> game_instance = parse_bff('showstopper_4.bff')
    """

    grid_data = []  # To store raw grid data from the file
    blocks = ['A', 'B', 'C']  # Valid block types
    available_blocks = []  # To store the types and counts of available block
    lasers = []  # To store laser objects
    points = []  # To store points that lasers need to intersect

    with open(file_path, 'r') as file:
        content = file.readlines()

    reading_grid = False
    for line in content:
        line = line.strip()
        print(line)
        if line.startswith('#') or not line:
            # This is a comment or empty line, skip it
            continue
        elif line == 'GRID START':
            reading_grid = True
        elif line == 'GRID STOP':
            reading_grid = False
        elif reading_grid:
            line = line.replace(" ", "")  # Remove spaces for grid data
            grid_data.append(line)
        elif line[0] in blocks:
            # This line indicates the number of a specific type of block
            try:
                block_type, count = line.split()
                available_blocks.extend([block_type
                                         for _ in range(int(count))])
            except ValueError:
                raise ValueError(f"Invalid block line: {line}")
        elif line.startswith('L'):
            # This line defines a laser
            try:
                _, x, y, vx, vy = line.split()
                lasers.append(Laser((int(x), int(y)), (int(vx), int(vy))))
            except ValueError:
                raise ValueError(f"Invalid laser line: {line}")
        elif line.startswith('P'):
            # This line defines a point
            try:
                _, x, y = line.split()
                points.append((int(x), int(y)))
            except ValueError:
                raise ValueError(f"Invalid point line: {line}")
    if not grid_data:
        raise ValueError("No grid data found in the file")

    rows = len(grid_data)
    cols = len(grid_data[0])
    grid_array = [[0 for i in range(cols)] for j in range(rows)]

    # Convert raw grid data to a 2D grid array
    for i, line in enumerate(grid_data):
        for j in range(cols):
            grid_array[i][j] = line[j:j + 1]
    block_object = Blocks(available_blocks)
    game = Game(grid_array, block_object, lasers, points)
    return game


def place_blocks(available_slots, blocks):
    """
    Generates all possible permutations of placing blocks
    onto the original board.

    Arguments:
    - available_slots (list): List of available slots on the board.
    - blocks (Blocks): The available blocks in the game.

    Returns:
    - perms (list): A list of all possible block placement permutations.

    Example:
    >> blocks = Blocks(['A', 'B', 'B', 'C', 'C', 'C'])
    >> slots = [(0, 0), (0, 1), (1, 1), (2, 2), (2, 2), (2, 2)]
    >> perms = place_blocks(slots, blocks)
    >> len(perms)
    60
    """
    # Extract block counts for reflection, opaque, refractive, and empty slots
    reflect = blocks.get_reflect()
    opaque = blocks.get_opaque()
    refract = blocks.get_refract()
    empty = len(available_slots) - reflect - opaque - refract

    # Creat a list of block symbols based on counts
    blocks = ['A'] * reflect + ['B'] * opaque + ['C'] * refract + ['o'] * empty

    # Generate all possible permutations of the block symbols
    perms = list(multiset_permutations(reflect * ('A',) +
                                       opaque * ('B',) +
                                       refract * ('C',) +
                                       empty * ('o',)))
    return perms


def find_all_placements(grid):
    """
    Finds all available slots on the grid where blocks can be placed.

    Arguments:
    - grid (list): The grid of the game.

    Returns:
    - available_positions (list): List of available slots on the grid.

    Example:
    >> grid = [[0, 'A', 0], ['B', 0, 'C']]
    >> find_all_placements(grid)
    [(0, 0), (0, 2), (1, 1)]
    """
    available_positions = []

    # Iterate through rows and columns to find 'o' (empty) slots
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'o':
                available_positions.append((i, j))
    return available_positions


def shoot_laser(grid, lasers):
    '''
    Shoot laser through the completed grid with blocks, and
    retain all the points that the laser passes through

    Arguments:
   - grid (list): The grid of the game.
   - lasers (list): The lasers in the game.

   Returns:
   - passed_points (list): List of points that the lasers pass through.

   Example:
   >> grid = [[0, 'A', 0], ['B', 0, 'C']]
   >> lasers = [Laser((1, 2), (1, -1)), Laser((3, 4), (0, -1))]
   >> shoot_laser(grid, lasers)
   [(2, 0), (2, 2)]
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

        def find_row_col(curr_pos, curr_dir):
            if curr_pos[0] % 2 == 0:  # if x coordinate is even
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
        if row_num >= len(grid) or col_num >= len(grid[0]):
            return
        interested_block = grid[row_num][col_num]
        # Identify what type of block is encountered
        if interested_block == 'A':  # reflect
            if curr_pos[0] % 2 == 0:
                # flip x only
                laser.change_direction((curr_dir[0]*(-1), curr_dir[1]))
            else:
                # flip y only
                laser.change_direction((curr_dir[0], curr_dir[1]*(-1)))
            # Need to account for the case where the starting points
            # are both reflect blocks for which
            # this code will keep recursively calling itself
            new_dir = laser.get_direction()
            temp_row_num, temp_col_num = find_row_col(curr_pos, new_dir)
            if temp_row_num < 0 or temp_col_num < 0:
                return
            if temp_row_num >= len(grid) or temp_col_num >= len(grid[0]):
                return
            new_block = grid[temp_row_num][temp_col_num]
            if new_block == 'A':
                return
            laser_step(laser, grid)
        elif interested_block == 'B':  # opaque, ray operation ends here
            return
        elif interested_block == 'C':  # refract
            new_pos = (curr_pos[0]+curr_dir[0], curr_pos[1]+curr_dir[1])
            if new_pos not in passed_points:
                passed_points.append(new_pos)
            new_laser = Laser(new_pos, curr_dir)
            laser_step(new_laser, grid)
            if curr_pos[0] % 2 == 0:
                laser.change_direction((curr_dir[0]*(-1), curr_dir[1]))
            else:
                laser.change_direction((curr_dir[0], curr_dir[1]*(-1)))
            # Need to account for the case where the starting points
            # are both reflect blocks for which
            # this code will keep recursively calling itself
            new_dir = laser.get_direction()
            temp_row_num, temp_col_num = find_row_col(curr_pos, new_dir)
            if temp_row_num < 0 or temp_col_num < 0:
                return
            if temp_row_num >= len(grid) or temp_col_num >= len(grid[0]):
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
        temp_laser = Laser(temp_pos, temp_dir)
        laser_step(temp_laser, grid)
    return passed_points


def check(curr_pos, grid):
    '''
    Checks if the current position is within the bounds of the grid.

    Arguments:
    - curr_pos (tuple): The current position as a tuple (x, y).
    - grid (list): The grid of the game.

    Returns:
    - in_bounds (bool): True if the position is within bounds, False otherwise.

    Example:
    >> grid = [[0, 'A', 0], ['B', 0, 'C']]
    >> check((2, 0), grid)
    True
    >> check((3, 0), grid)
    False
    '''
    # Calculate the total number of rows and columns based on the grid
    rows = len(grid)*2
    cols = len(grid[0])*2

    # Check if the current position is within the calculated bounds
    if curr_pos[1] > rows or curr_pos[0] > cols:
        return False

    if curr_pos[1] < 0 or curr_pos[0] < 0:
        return False

    return True


def check_solution(passed_points, required_points):
    '''
    Check if the current solution contains all points required

    Arguments:
   - passed_points (list): List of points that the lasers have passed through.
   - required_points (list): List of points that the lasers need to intersect.


   Returns:
   - solution_found (bool): True if the solution is found, False otherwise.


   Example:
   >> passed_points = [(0, 1), (1, 1), (2, 1), (2, 2)]
   >> required_points = [(0, 1), (1, 1), (2, 2)]
   >> check_solution(passed_points, required_points)
   True
   >> required_points = [(0, 1), (2, 2), (3, 3)]
   >> check_solution(passed_points, required_points)
   False

    '''
    for point in required_points:
        if point not in passed_points:
            return False
    return True


def initialize_board(org_grid, available_slots, perm):
    '''
    Initializes the board with the given permutation of block placements.


   Arguments:
   - org_grid (list): The original grid of the game.
   - available_slots (list): List of available slots on the grid.
   - perm (list): Permutation of block placements.


   Returns:
   - new_grid (list): The new grid with the block placements.


   Example:
   >> org_grid = [[0, 'A', 0], ['B', 0, 'C']]
   >> available_slots = [(0, 0), (0, 2), (1, 1)]
   >> perm = ['A', 'B', 'C']
   >> new_grid = initialize_board(org_grid, available_slots, perm)
   >> new_grid
   [['A', 'A', 'B'], ['B', 'C', 'C']]

    '''
    new_grid = org_grid
    for i, slot in enumerate(available_slots):
        new_grid[slot[0]][slot[1]] = perm[i]
    return new_grid


def solve(file_path):
    """
   Solves a game by creating a game instance from the given file,
   finding a solution, and saving it to a new .bff file.


   Arguments:
   - file_path (str): The path of the .bff file.


   Example:
   >> solve('showstopper_4.bff')
    """
    # Parse the .bff file to create a game instance
    new_game = parse_bff(file_path)
    grid = new_game.get_grid()
    slots_available = find_all_placements(grid)
    blocks = new_game.get_blocks()
    all_permutations = place_blocks(slots_available, blocks)
    lasers = new_game.get_lasers()
    target_points = new_game.get_points()

    # Iterate through all permutations and test each one
    for perm in all_permutations:
        test_grid = initialize_board(grid, slots_available, perm)
        test_points = shoot_laser(test_grid, lasers)

    # Check if the current solution matches the target points
        if check_solution(test_points, target_points):
            # Create the solution filenamepycodestyle lazor.py
            solution_file = f"solution_{file_path}"
        # Save the solution to the solution file
            with open(solution_file, "w") as file:
                file.write("GRID START\n")
                for row in test_grid:
                    # Convert each row of the grid back to a string with spaces
                    file.write(" ".join(map(str, row)) + "\n")
                file.write("GRID STOP\n")
            print(f"Solution found! Solution saved to {solution_file}")
            return

    print("No solution found")


class TestLazorProject (unittest.TestCase):
    """
    Performs unit tests for all functions in this project

    Args:
        unittest (TestCase): uses the unittest module in Python
    """
    def setUp(self):
        self.grid = [['o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o'],
                     ['o', 'o', 'o', 'o'], ['o', 'o', 'o', 'o']]
        self.blocks = Blocks(['A', 'A', 'C'])
        self.laser = Laser((3, 4), (1, -1))
        self.laser2 = Laser((2, 7), (1, -1))
        self.lasers = [self.laser2]
        self.points = [(3, 0), (4, 3), (2, 5), (4, 7)]
        self.game = Game(self.grid, self.blocks, self.lasers, self.points)

    def test_get_reflect(self):
        """
        Tests the get_reflect() function within class 'Blocks'
        """
        self.assertEqual(self.blocks.get_reflect(), 2,
                         'The get_reflect function is wrong')

    def test_get_opaque(self):
        """
        Tests the get_opaque() function within class 'Blocks'
        """
        self.assertEqual(self.blocks.get_opaque(), 0,
                         'The get_opaque function is wrong')

    def test_get_refract(self):
        """
        Tests the get_reflect() function within class 'Blocks'
        """
        self.assertEqual(self.blocks.get_refract(), 1,
                         'The get_refract function is wrong')

    def test_get_position(self):
        """
        Tests the get_position() function within class 'Laser'
        """
        self.assertEqual(self.laser.get_position(), (3, 4),
                         'The get_position function is wrong')

    def test_get_direction(self):
        """
        Tests the get_direction() function within class 'Laser'
        """
        self.assertEqual(self.laser.get_direction(), (1, -1),
                         'The get_direction function is wrong')

    def test_change_position(self):
        """
        Tests the change_position() function within class 'Laser'
        """
        self.laser.change_position((4, 5))
        self.assertEqual(self.laser.get_position(), (4, 5),
                         'The change_position function is wrong')

    def test_change_direction(self):
        """
        Tests the change_direction() function within class 'Laser'
        """
        self.laser.change_direction((1, 1))
        self.assertEqual(self.laser.get_direction(), (1, 1),
                         'The change_direction function is wrong')

    def test_get_grid(self):
        """
        Tests the get_grid() function within class 'Game'
        """
        correct_grid = self.grid
        self.assertEqual(self.game.get_grid(), correct_grid,
                         'The get_grid function is wrong')

    def test_get_blocks(self):
        """
        Tests the get_blocks() function within class 'Game'
        """
        correct_blocks = self.blocks
        self.assertEqual(self.game.get_blocks(), correct_blocks,
                         'The get_blocks function is wrong')

    def test_get_lasers(self):
        """
        Tests the get_lasers() function within class 'Game'
        """
        correct_lasers = self.lasers
        self.assertEqual(self.game.get_lasers(), correct_lasers,
                         'The get_lasers function is wrong')

    def test_get_points(self):
        """
        Tests the get_points() function within class 'Game'
        """
        correct_points = self.points
        self.assertEqual(self.game.get_points(), correct_points,
                         'The get_points function is wrong')

    def test_parse_bff(self):
        """
        Tests the parse_bff(file_path) function
        """
        test_file_path = 'mad_1.bff'
        self.assertIsInstance(parse_bff(test_file_path), Game,
                              'The parse_bff function is wrong')

    def test_place_blocks(self):
        """
        Tests the place_blocks(available_slots, blocks) function
        """
        test_slots = [(0, 0), (0, 1), (0, 2)]
        test_perms = place_blocks(test_slots, self.blocks)
        self.assertIn(['A', 'A', 'C'], test_perms)
        self.assertIn(['A', 'C', 'A'], test_perms)
        self.assertEqual(len(test_perms), 3,
                         'The place_blocks function is wrong')

    def test_find_all_placements(self):
        """
        Test the find_all_placements(grid) function
        """
        test_grid = [['o', 'B', 'o'],
                     ['A', 'x', 'o'],
                     ['C', 'o', 'o']]
        correct_result = [(0, 0), (0, 2), (1, 2), (2, 1), (2, 2)]
        self.assertEqual(find_all_placements(test_grid), correct_result,
                         'The find_all_placement funcion is wrong')

    def test_shoot_laser(self):
        """
        Test the shoot_laser(grid, lasers) function
        """
        test_grid = [['o', 'B', 'o'],
                     ['A', 'x', 'o'],
                     ['C', 'o', 'o']]
        test_laser_1 = Laser((4, 3), (-1, -1))
        correct_points_1 = [(3, 2)]
        self.assertEqual(shoot_laser(test_grid, [test_laser_1]),
                         correct_points_1,
                         'The shoot_laser method is wrong')
        test_laser_2 = Laser((3, 4), (-1, -1))
        correct_points_2 = [(2, 3), (3, 2)]
        self.assertEqual(shoot_laser(test_grid, [test_laser_2]),
                         correct_points_2,
                         'The shoot laser method is wrong')
        test_laser_3 = Laser((3, 4), (-1, 1))
        correct_points_3 = [(2, 5), (1, 6), (3, 6)]
        self.assertEqual(shoot_laser(test_grid, [test_laser_3]),
                         correct_points_3,
                         'The shoot_laser method is wrong')

    def test_check(self):
        """
        Test the check(curr_pos, grid) function
        """
        self.assertTrue(check((2, 0), self.grid),
                        'The function cannot detect a point on the grid')
        self.assertFalse(check((-1, 0), self.grid),
                         'The function cannot detect a point not on the grid')
        self.assertFalse(check((9, 5), self.grid),
                         'The function cannot detect a point not on the grid')

    def test_check_soluition(self):
        """
        Test the check_solution(passed_points, required_points) function
        """
        points_1 = [(3, 0), (4, 3), (2, 5), (4, 7), (1, -1)]
        points_2 = [(3, 0), (4, 2), (1, 8), (9, 7)]
        self.assertTrue(check_solution(points_1, self.points),
                        'The check_solution function is wrong')
        self.assertFalse(check_solution(points_2, self.points),
                         'The check_solution function is wrong')

    def test_initialize_board(self):
        """
        Test the initialize_board(org_grid, available_slots, perm) function
        """
        test_slots = [(0, 0), (0, 3), (1, 3), (2, 1)]
        test_perm = ['A', 'C', 'B', 'A']
        correct_grid = [['A', 'o', 'o', 'C'],
                        ['o', 'o', 'o', 'B'],
                        ['o', 'A', 'o', 'o'],
                        ['o', 'o', 'o', 'o']]
        self.assertEqual(initialize_board(self.grid, test_slots, test_perm),
                         correct_grid,
                         'The initialize_board function is wrong')


if __name__ == "__main__":
    # Test the solve function with one of the files
    file_path = 'showstopper_4.bff'
    solve(file_path)
    unittest.main()
