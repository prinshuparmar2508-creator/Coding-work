data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [], 'E': [], 'F': [], 'G': []
}

goal = input("goal likh lawde: ").strip().upper()

queue = ['A']
visited = ['A']
order = []

def bfs(queue ,visited):

    while queue:
        node = queue.pop(0)
        order.append(node)

        if node == goal:
            print(order)
            print("The goal has been found")
            return 
        
        for next_gen in data[node]:
            if next_gen not in visited:
                visited.append(next_gen)
                queue.append(next_gen)
    else:
        print("Goal not found in data")

bfs(queue ,visited)

