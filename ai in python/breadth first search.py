graph = {"A": ["B", "C"],
         "B": ["D", "E"],
         "C": ["F", "G"],
         "D": ["H"],
         "E": ["I"],
         "F": ["J"],
         "G": [],
         "H": [],
         "I": [],
         "J": []}

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        c = queue.pop(0)
        print(c, end=" ")
        for succesor in graph[c]:
            if succesor not in visited:
                visited.append(succesor)
                queue.append(succesor)
print("The result for breadth first search is: ")
bfs(visited, graph, "A")
