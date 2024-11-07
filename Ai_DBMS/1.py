#PRACTICAL 1: BFS & DFS
#BREADTH-FIRST SEARCHING IN GRAPH
# Practical No. 01
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)    #dequeue node from front to the queue
    print (m, end = " ") #print current node
    for neighbour in graph[m]: #loop through current node neighbour
      if neighbour not in visited: #it neighbor hasnt been visited
        visited.append(neighbour) #mark it as visited
        queue.append(neighbour) #add it as queue
# Driver Code
print("Following is the Breadth-First Search :- ")
bfs(visited, graph, '5')    # function calling




# DEPTH-FIRST SEARCH
# Practical No. 01
# Using a Python dictionary to act as an adjacency list
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited: #check if node is not visited
        print (node) #print current node
        visited.add(node) #mark node as visited 
        for neighbour in graph[node]: #recursively visit each neighbor
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search :- ")
dfs(visited, graph, '5')
