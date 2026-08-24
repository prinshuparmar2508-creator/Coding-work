goal=str(input("Enter gaol:"))
goal=goal.upper()
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
        if c==goal:
            print("\nThe goal is found:")
            return
        for succesor in graph[c]:
            if succesor not in visited:
                visited.append(succesor)
                stack.append(succesor)
    else:
        print("\nThe goal isn't here")

dfs(visited,graph,'A')
print("\n depth first search implementation")