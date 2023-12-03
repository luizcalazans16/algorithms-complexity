import heapq

class Node:
    def __init__(self, x, y, cost, estimated_cost):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristic = estimated_cost
        self.parent = None

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def read_map(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        width, height = map(int, lines[0].split())
        start_x, start_y = map(int, lines[1].split())
        grid = [list(map(int, line.split())) for line in lines[2:]]
    return width, height, start_x, start_y, grid

def estimate_cost(x, y, target_x, target_y):
    return abs(x - target_x) + abs(y - target_y)

def path_finder(width, height, start_x, start_y, target_x, target_y, grid):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    open_set = [Node(start_x, start_y, 0, estimate_cost(start_x, start_y, target_x, target_y))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.x == target_x and current_node.y == target_y:
            path = [(current_node.x, current_node.y)]
            while current_node.parent:
                path.append((current_node.parent.x, current_node.parent.y))
                current_node = current_node.parent
            path.reverse()
            return path, current_node.cost

        closed_set.add((current_node.x, current_node.y))

        for dx, dy in directions:
            neighbor_x, neighbor_y = current_node.x + dx, current_node.y + dy

            if 0 <= neighbor_x < width and 0 <= neighbor_y < height and (neighbor_x, neighbor_y) not in closed_set:
                if grid[neighbor_y][neighbor_x] >= 0:
                    neighbor = Node(neighbor_x, neighbor_y, current_node.cost + 1,
                                    estimate_cost(neighbor_x, neighbor_y, target_x, target_y))
                    neighbor.parent = current_node
                    heapq.heappush(open_set, neighbor)

    return None, float('inf')

def main():
    file_path = "map.txt"
    width, height, start_x, start_y, grid = read_map(file_path)

    print(f"Mapa:\n{grid}")
    target_x, target_y = map(int, input("Digite as coordenadas do destino (ex: 3 5): ").split())

    path, cost = path_finder(width, height, start_x, start_y, target_x, target_y, grid)

    if path:
        print(f"Caminho encontrado com custo {cost}: {' '.join([f'{x},{y}' for x, y in path])}")
    else:
        print("Caminho não encontrado.")

if __name__ == "__main__":
    main()
