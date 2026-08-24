graph = {"A": ["B", "C"],
         "B": ["D", "E"],
         "C": ["F"],
         "D": [],
         "E": [],
         "F": [],
        }

visited = []
stack = []

def dfs (visited,graph,node):
    visited.append(node)
    stack.append(node)
    while stack:
        c=stack.pop()
        print(c,end=" ")
        for succesor in graph[c]:
            if succesor not in visited:
                visited.append(succesor)
                stack.append(succesor)

dfs(visited,graph,'A')