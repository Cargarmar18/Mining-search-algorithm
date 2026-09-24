from search_minimal import (
    Problem,
    breadth_first_graph_search,
    depth_first_graph_search,
    astar_search,
)


class MinerProblem(Problem):

    def __init__(self, initial, goal, matrix):
        '''we need tuples to keep track of visited nodes
        and to avoid looping and errors'''
        self.initial = tuple(initial)
        self.goal = tuple(goal)
        self.matrix = matrix

    def actions(self, state):
        '''actions per node'''
        return ["move", "turn_left", "turn_right"]

    def result(self, state, action):
        row, col, direction = state

        if action == "turn_left":
            return (row, col, (direction - 1) % 8)

        if action == "turn_right":
            return (row, col, (direction + 1) % 8)

        if action == "move":
            '''we need to guarantee that there is a position where we can move to
            we can do this by checking the maximum size of the matrix in both rows
            and columns and constraint the movement. We cannot move outside the matrix'''
            rows = len(self.matrix)
            cols = len(self.matrix[0])

            if direction == 0:   #north
                new_row, new_col = row - 1, col
            elif direction == 1: #northeast
                new_row, new_col = row - 1, col + 1
            elif direction == 2: #east
                new_row, new_col = row, col + 1
            elif direction == 3: #southeast
                new_row, new_col = row + 1, col + 1
            elif direction == 4: #south
                new_row, new_col = row + 1, col
            elif direction == 5: #southwest
                new_row, new_col = row + 1, col - 1
            elif direction == 6: #west
                new_row, new_col = row, col - 1
            elif direction == 7: #northwest
                new_row, new_col = row - 1, col - 1
            else:
                return (row, col, direction)

            if 0 <= new_row < rows and 0 <= new_col < cols:
                return (new_row, new_col, direction)
            
        return (row, col, direction)

    def goal_test(self, state):
        row, col, _ = state
        goal_row, goal_col, goal_direction = self.goal

        '''in case that the direction is 8 any direction is valid'''
        if goal_direction == 8:
            return (row, col) == (goal_row, goal_col)
        
        return state == self.goal

    def path_cost(self, c, state1, action, state2): 
        '''state1: previous state /// state2: accumulated state'''
        if action in ("turn_left", "turn_right"):
            return c + 1


        row, col, _ = state2
        return c + self.matrix[row][col]

    def h(self, node):
        '''define heuristic for A*'''
        row_g, col_g, _ = self.goal
        row, col, _ = node.state
        return abs(row_g - row) + abs(col_g - col)


def print_search_report(label, node, explored, frontier):

    states = node.path_states()
    actions = node.solution()

    print(f"\n=== {label} ===")

    for i in range(len(states)):
        print(f"Node {i}: {states[i]}")
        print(f"Operator: {actions[i-1]}")

    print(f"\n- - - - - - -")

    print(f"Total number of items explored in list: {explored} Total")
    print(f"Number of items in frontier: {frontier}")
    print(f"Total path cost: {node.path_cost}")
    print(f"Total path depth: {node.depth}")
    

def matrix_reader(path):
    '''we should return the matrix. initial and goals parsed'''
    with open(path, encoding='utf-8') as f:
        '''In case we have issues with indented lines we do this'''
        line = f.readline()
        while not line.strip():
            line = f.readline()

        '''get the numbers of the line mapped to integers and stored in lists'''
        rows, _ = map(int, line.split())

        matrix = []
        '''each line is a row of the matrix'''
        for _ in range(rows):
            line = f.readline()
            while not line.strip():
                line = f.readline()

            matrix.append(list(map(int, line.split())))

        line = f.readline()
        while not line.strip():
            line = f.readline()
        initial = list(map(int, line.split()))

        line = f.readline()
        while line and not line.strip():
            line = f.readline()
        goal = list(map(int, line.split())) 

    return matrix, initial, goal


def main():

    path = input("Path of the file of the miner problem to solve: ").strip()

    matrix, initial, goal = matrix_reader(path)
    problem = MinerProblem(initial, goal, matrix) #(initial, goal)

    bfs_node, bfs_explored, bfs_frontier = breadth_first_graph_search(problem)
    dfs_node, dfs_explored, dfs_frontier = depth_first_graph_search(problem)
    astar_node, astar_explored, astar_frontier = astar_search(problem, h=problem.h)

    print_search_report("BFS", bfs_node, bfs_explored, bfs_frontier)
    print_search_report("DFS", dfs_node, dfs_explored, dfs_frontier)
    print_search_report("A*", astar_node, astar_explored, astar_frontier)


if __name__ == "__main__":
    main()
