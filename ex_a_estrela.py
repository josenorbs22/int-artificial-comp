

class Node():
    """Uma classe de nodo para A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Retorna uma lista de tuplas como um caminho para o início e final dados no labirinto dado"""

    # Cria um nodo de começo e final
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Inicializa tanto a lista aberta quanto a fechada
    open_list = []
    closed_list = []

    # Adiciona o nodo de começo
    open_list.append(start_node)

    # Repete até achar o final
    while len(open_list) > 0:

        # Pega o nodo atual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Tira o índice atual da lista aberta e o adiciona a lista fechada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Achou o objetivo
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Retorna o caminho invertido

        # Gera filhos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Quadrados adjacentes

            # Pega a posição do nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Certificar de que está dentro do alcance
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Certificar que é um terreno andável
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Cria um novo nodo
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Repete pelos filhos
        for child in children:

            # Filho está dentro da lista fechada?
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Cria os valores f, g e h
            child.g = current_node.g + 1
            child.h = abs(child.position[0] - end_node.position[0]) + abs((child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            # Filho já está na lista aberta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Adiciona o filho na lista aberta
            open_list.append(child)

def greedy(maze, start, end):
    """Retorna uma lista de tuplas como um caminho para o início e final dados no labirinto dado"""

    # Cria um nodo de começo e final
    start_node = Node(None, start)
    start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.h = end_node.f = 0

    # Inicializa tanto a lista aberta quanto a fechada
    open_list = []
    closed_list = []

    # Adiciona o nodo de começo
    open_list.append(start_node)

    # Repete até achar o final
    while len(open_list) > 0:

        # Pega o nodo atual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Tira o índice atual da lista aberta e o adiciona a lista fechada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Achou o objetivo
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Retorna o caminho invertido

        # Gera filhos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Quadrados adjacentes

            # Pega a posição do nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Certificar de que está dentro do alcance
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Certificar que é um terreno andável
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Cria um novo nodo
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Repete pelos filhos
        for child in children:

            # Filho está dentro da lista fechada?
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Cria os valores f e h
            child.h = abs(child.position[0] - end_node.position[0]) + abs((child.position[1] - end_node.position[1]))
            child.f = child.h

            # Filho já está na lista aberta
            for open_node in open_list:
                if child == open_node:
                    continue

            # Adiciona o filho na lista aberta
            open_list.append(child)


def main():
    n = 10
    m = 10
    maze_ex1 = [[0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 1, 1, 0],
            [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 0]]

    start_ex1 = (1, 0)
    end_ex1 = (6, 9)

    maze_ex2 = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]
    
    start_ex2 = (3, 0)
    end_ex2 = (9, 9)

    maze_astar_2 = maze_ex2
    maze_greedy = maze_ex2
    x = 0

    path_astar_1 = astar(maze_ex1, start_ex1, end_ex1)
    path_astar_2 = astar(maze_ex2, start_ex2, end_ex2)
    path_greedy = greedy(maze_ex2, start_ex1, end_ex2)
    print(path_astar_1)
    print(path_astar_2)
    print(path_greedy)

    for i in range(0,n):
        for j in range(0,m):
            for locPath in path_astar_1:
                locMaze = str(i)+str(j)
                locPathFinal = ""
                for item in locPath:
                    locPathFinal = locPathFinal + str(item)

                    if(locPathFinal == locMaze):
                        maze_ex1[i][j] = 2

    for i in range(0,n):
        for j in range(0,m):
            for locPath in path_astar_2:
                locMaze = str(i)+str(j)
                locPathFinal = ""
                for item in locPath:
                    locPathFinal = locPathFinal + str(item)

                    if(locPathFinal == locMaze):
                        maze_astar_2[i][j] = 2

    for i in range(0,n):
        for j in range(0,m):
            for locPath in path_greedy:
                locMaze = str(i)+str(j)
                locPathFinal = ""
                for item in locPath:
                    locPathFinal = locPathFinal + str(item)

                    if(locPathFinal == locMaze):
                        maze_greedy[i][j] = 2

    print("-----------------")
    print("A* labirinto 1")
    for i in maze_ex1:
        print(i)

    print("A* labirinto 2")
    for i in maze_astar_2:
        print(i)

    print("-----------------")
    print("Guloso")
    for i in maze_greedy:
        print(i)
                


if __name__ == '__main__':
    main()