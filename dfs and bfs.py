myGraph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def my_dfs(graph, start_node):
    visited = list()    #방문한 노드
    stack = list()      #방문할 노드
    stack.append(start_node)

    while stack:
        node = stack.pop() #stack의 끝에서 하나씩 꺼내기
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    
    print(visited)

my_dfs(myGraph, 'G')

def my_bfs(graph, start_node):
    visited=list()
    stack=list()
    stack.append(start_node)

    while stack:
        node=stack.pop(0)
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    
    print(visited)


my_bfs(myGraph, 'G')