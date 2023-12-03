import heapq

class Node:
    def __init__(self, x, y, cost, heuristic):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic
        self.parent = None

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def heuristic_cost(x, y, goal_x, goal_y):
    return abs(goal_x - x) + abs(goal_y - y)

def get_neighbors(x, y, width, height, grid):
    neighbors = []
    if x > 0 and grid[y][x - 1] != -1:
        neighbors.append((x - 1, y))
    if x < width - 1 and grid[y][x + 1] != -1:
        neighbors.append((x + 1, y))
    if y > 0 and grid[y - 1][x] != -1:
        neighbors.append((x, y - 1))
    if y < height - 1 and grid[y + 1][x] != -1:
        neighbors.append((x, y + 1))
    return neighbors

def a_star(start_x, start_y, goal_x, goal_y, width, height, grid):
    start_node = Node(start_x, start_y, 0, heuristic_cost(start_x, start_y, goal_x, goal_y))
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.x == goal_x and current_node.y == goal_y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add((current_node.x, current_node.y))

        for neighbor_x, neighbor_y in get_neighbors(current_node.x, current_node.y, width, height, grid):
            if (neighbor_x, neighbor_y) in closed_set:
                continue

            neighbor_node = Node(neighbor_x, neighbor_y, current_node.cost + 1, heuristic_cost(neighbor_x, neighbor_y, goal_x, goal_y))
            neighbor_node.parent = current_node

            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)
    
    return None

def read_map(file_name):
    with open(file_name, 'r') as file:
        width, height = map(int, file.readline().split())
        start_x, start_y = map(int, file.readline().split())
        grid = []
        for _ in range(height):
            row = list(map(int, file.readline().split()))
            grid.append(row)
        return width, height, start_x, start_y, grid

def main():
    file_name = 'map.txt'
    width, height, start_x, start_y, grid = read_map(file_name)

    goal_x, goal_y = map(int, input("Digite as coordenadas do destino (x y): ").split())

    path = a_star(start_x, start_y, goal_x, goal_y, width, height, grid)

    if path:
        cost = len(path) - 1
        print(f"Custo total: {cost}")
        print("Caminho:", end=" ")
        for x, y in path:
            print(f"{x},{y}", end=" ")
    else:
        print("Não há caminho possível.")

if __name__ == "__main__":
    main()
