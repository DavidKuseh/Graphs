# import Graph and Queue
from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # create graph
    graph = Graph()
    
    # add parent and child vertices, and edge
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    # create queue  
    q = Queue()
    # enqueue starting node(input)
    q.enqueue([starting_node])
    
    # longest path initialised with value set to 1(to handle case of no parent)
    longest_path_length = 1
    
    # set earliest ancestor to 1(to handle case of no parent)
    earliest_ancestor = -1
    
    # while queue is not empty set the last node as the current node
    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]
        
        # if path length is greater/equal to longest path length and current node is less than earliest ancestor,
        # or path length is greater than longest path length
        if (len(path) >= longest_path_length and current_node < earliest_ancestor) or len(path) > longest_path_length:
            # set path length to longest path length
            longest_path_length = len(path)
            # set current node to earliest ancestor
            earliest_ancestor = current_node
        
        # current node is added to vertices set    
        neighbors = graph.vertices[current_node]
        # each ancestor is appended to copy of path. Enqueue copy of path to queue
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            q.enqueue(path_copy)
            
    # return earliest ancestor (farthest node from input node)        
    return earliest_ancestor
      