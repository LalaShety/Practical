class Node:
    def __init__(self, no):
        self.dist = [float('inf')] * no  # Initialize distances with infinity
        self.from_node = [0] * no        # Initialize from_node with 0


def main():
    no = int(input("Enter number of nodes: "))

    # Create a distance matrix (2D array)
    dm = [[0 if i == j else float('inf') for j in range(no)] for i in range(no)]

    # Create a list of Node objects to store routing information
    route = [Node(no) for _ in range(no)]

    # Input the distance matrix
    print("Enter the distance matrix:")
    for i in range(no):
        for j in range(no):
            if i != j:
                dm[i][j] = int(input(f"Distance from node {i+1} to node {j+1}: "))
            route[i].dist[j] = dm[i][j]
            route[i].from_node[j] = j

    # Distance Vector Algorithm (Bellman-Ford Algorithm)
    flag = True
    while flag:
        flag = False
        for i in range(no):
            for j in range(no):
                for k in range(no):
                    if route[i].dist[j] > route[i].dist[k] + route[k].dist[j]:
                        route[i].dist[j] = route[i].dist[k] + route[k].dist[j]
                        route[i].from_node[j] = k
                        flag = True

    # Display routing information
    for i in range(no):
        print(f"Router info for router: {i + 1}")
        print("Dest\tNext Hop\tDist")
        for j in range(no):
            print(f"{j + 1}\t{route[i].from_node[j] + 1}\t\t{route[i].dist[j]}")

if __name__ == "__main__":
    main()
