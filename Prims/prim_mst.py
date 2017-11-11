from undirected_graph import Graph
import undirected_graph_files_equal
import heapq


def write_tree_edges_to_file(edges, filename):
    # TODO write out the edges, one per line. The same format as produced by generate_mst_input
    with open(filename, mode='w') as f:
        print ("H: ", edges)
        for v1, v2, w in edges:
            f.write("{} {} {}\n".format(v1, v2, w))


# Don't change this function's name or the arguments it takes. Also, do not change
# that it writes out the results at the end.
# This is the full contract of you code (this function in this file). Otherwise,
# please feel free to create helpers, modify provided code, create new helper files, etc.
# Whatever you turn in is what we will grade (ie we won't provide any files or overwrite
# any of yours)
# Have fun!
def compute_mst(filename):
    '''Use Prim's algorithm to compute the minimum spanning tree of the weighted undirected graph
    described by the contents of the file named filename.'''

    g = undirected_graph_files_equal.read_weighted_undirected_graph(filename)
    totalNodes = list(g.get_nodes())

    currNode = totalNodes[0] #set start node
    tree = set()
    q = []
    visited = [currNode]
    #possibleEdges = []
    unique = False

    print(list((g.edges.get(currNode)).keys()))

    while (len(visited) < len(totalNodes)): #while there are still more to be visited
        for node in list((g.edges.get(currNode)).keys()):
            lineWeight = (g.attributes_of(currNode, node).get('weight'))
            tup1 = (lineWeight, currNode, node)
            heapq.heappush(q, tup1)
        weight, startNode, endNode = heapq.heappop(q)
        if (endNode not in visited):
            tup2 = (startNode, endNode, weight)
            tree.add(tup2)
            currNode = endNode
            visited.append(currNode)
        else:
            while(unique == False):
                weight, startNode, endNode = heapq.heappop(q)
                if (endNode not in visited):
                    tup2 = (startNode, endNode, weight)
                    tree.add(tup2)
                    currNode = endNode
                    visited.append(currNode)
                    unique == True
                    break
        print("FinalTree: ", tree)


    visited = []

    tree_edges = tree




    # TODO compute the edges of a minimum spanning tree
    write_tree_edges_to_file(tree_edges, filename + '.mst')

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    compute_mst(filename)
    print(undirected_graph_files_equal.graph_files_equal(sys.argv[2], sys.argv[3]))
