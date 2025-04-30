from collections import deque
from heapq import heappush, heappop

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ##heap with total weight, number of edges, and current node
    heap = [(0, 0, source)]

    result = {}

    while heap:
        weight, edges, node = heappop(heap)
        #check if we have already visited this node
        if node in result:
            previous_weight, previous_edges = result[node]
            #check if we have found a shorter path or a path with the same weight but more edges
            if weight > previous_weight or (weight == previous_weight and edges > previous_edges):
                continue
              
        result[node] = (weight, edges)
        #add all neighbors to the heap
        for neighbor, edge_weight in graph.get(node, []):
          
            #check if we have already visited this neighbor
            if neighbor not in result or (weight + edge_weight, edges + 1) < result[neighbor]:
              heappush(heap, (weight + edge_weight, edges + 1, neighbor))

    return result

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

    ###TODO
    parents = {}
    queue = deque([source])

  
    while queue:
        node = queue.popleft()
        #check if we have already visited this node
        for neighbor in graph.get(node, []):
            #check if we have already visited this neighbor and if it is not the source node
            if neighbor not in parents and neighbor != source:
              parents[neighbor] = node
              queue.append(neighbor)
    return parents
    

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    node = destination
    while node in parents:
        path.append(node)
        node = parents[node]
    path.append(node)  # Add the source node
    path.reverse()
    return " -> ".join(path)
  

