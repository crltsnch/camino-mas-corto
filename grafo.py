# Crear un grafo vacío
graph = {}

# Agregar nodos al grafo y bordes
graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C"]

# Funcion para buscar el camino mas corto entre dos nodos
def shortest_path(graph, start, goal):
    # Crear una cola y agregar el nodo inicial
    cola = [[start]]
    # Crear una lista para almacenar los nodos visitados
    visited = []
    # Mientras la cola no esté vacía
    while cola:
        # Tomar el primer camino de la cola
        path = cola.pop(0)
        # Tomar el ultimo nodo del camino
        node = path[-1]
        # Si el nodo no ha sido visitado
        if node not in visited:
            neighbours = graph[node]
            # Crear una copia de cada camino en la cola
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                cola.append(new_path)
                # Si el vecino es el nodo objetivo
                if neighbour == goal:
                    return new_path
            # Marcar el nodo como visitado
            visited.append(node)
    # Si no se encuentra un camino, retornar None
    return None