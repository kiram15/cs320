import graph

def read_topo_sort_from_file(filename):
    """This reads the first line of the file. In a topological sort solution file,
    the first line holds the nodes in topological sort order on the first line,
    separated by whitespace."""
    with open(filename) as f:
        string = f.readline()
    return string


def parse_tps(tps_str):
    """ Gets a string of ordering of nodes for topological
    ordering and creates a list of integers from that. """
    return [int(x) for x in tps_str.split()]


def contains_sink_node(graph):
    """ Checks if there is a node without outgoing edge. """
    # empty collections are boolean false, so this asks if all
    # nodes have a non-empty set of neighbors (outgoing edges)
    return all(graph[i] for i in graph)


def check_TPS(graph, tps):
    """ Takes a out-edge graph dictionary and a list of integers for
    topological ordering and checks if that topological ordering is correct. """
    for i in reversed(range(len(tps))):
        for j in range(i):
            if tps[j] in graph[tps[i]]:
                print("Fault: There is a backward edge from ", tps[i], " to ", tps[j])
                return False
    if len(graph.keys()) != len(tps):
        return False
    return True


def write_tps_to_file(tps, filename):
    with open('output_' + filename, 'w') as file:
        for node in tps:
            file.write(node + ' ')

def visit(node, startDict, startGraph, stringTps):
    if startDict[node] == 'B': return #if it's done
    if startDict[node] == 'G': #if there's a backwards edge
        print("Not valid topological sort. DAG exists")
        sys.exit()

    startDict[node] = 'G'
    #visit all of its outDegrees
    for dependentNode in startGraph[node]:
        visit(dependentNode, startDict, startGraph, stringTps)
    startDict[node]= 'B'
    stringTps.append(str(node))

def compute_tps(filename):
    startGraph = graph.read_graph(filename)  #tracks keys and outDegrees
    startDict = {}
    # declaring them all as white to start
    for i in startGraph.keys():
        startDict[i] = 'W'

    stringTps = [] #backwards topological sort
    #while there are unvisited nodes
    while 'W' in startDict.values():
        for node in startDict:
            if (startDict[node] == 'W'):
                visit(node, startDict, startGraph, stringTps)

    #reverse sort because to add in at the beginning would increase complexity
    stringTps.reverse()
    write_tps_to_file(stringTps, filename)

if __name__ == '__main__':
    """ Write code here to run compute_tps for your testing purposes"""
    import sys
    filename = sys.argv[1]
    compute_tps(filename)
