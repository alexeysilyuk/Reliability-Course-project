import random
from collections import deque, namedtuple
import itertools

#DIJKSTRA implementation start -----------------------

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                if(cost==0):
                    break
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path



#DIJKSTRA implementation end -----------------------

nodes=["1","2","3"]

forward_edges=[("1", "2", 0), ("2", "3", 0), ("3", "4", 0),("4", "5", 0),("1", "5", 0),
        ("6", "7", 0), ("7", "8", 0), ("8", "9", 0),("9", "10", 0),("10", "11", 0),
        ("11", "12", 0), ("12", "13", 0), ("13", "14", 0),("14", "15", 0),("15", "6", 0),
        ("16", "17", 0), ("17", "18", 0), ("18", "19", 0),("19", "20", 0),("20", "16", 0),
        ("15", "16", 0), ("7", "17", 0), ("9", "18", 0),("11", "19", 0),("13", "20", 0),
        ("1", "8", 0), ("2", "10", 0), ("3", "12", 0),("4", "14", 0),("5", "6", 0)]

backward_edges=[("2", "1", 0), ("3", "2", 0), ("4", "3", 0),("5", "4", 0),("5", "1", 0),
        ("7", "6", 0), ("8", "7", 0), ("9", "8", 0),("10", "9", 0),("11", "10", 0),
        ("12", "11", 0), ("13", "12", 0), ("14", "13", 0),("15", "14", 0),("6", "15", 0),
        ("17", "16", 0), ("18", "17", 0), ("19", "18", 0),("20", "19", 0),("16", "20", 0),
        ("16", "15", 0), ("17", "7", 0), ("18", "9", 0),("19", "11", 0),("20", "13", 0),
        ("8", "1", 0), ("10", "2", 0), ("12", "3", 0),("14", "4", 0),("6", "5", 0)]

edges=[]
r=0
p_list=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,0.99]
p=0.0
x=0
terminals=['1','3','17']


def randomX():
    return random.random()


def getNodes():
    # nodes.append("1")
    # nodes.append("2")
    # nodes.append("3")
    # node = input("Enter node number:( 0 for stop) ")
    # while node != 0:
    #     if node not in nodes:
    #         nodes.append(node)
    #     node = input("Enter node number: ")

    return 1
    # print nodes

def getEdges():
    # edge = input("Enter edge number:( 0 for stop) ")
    # edge = "(10, 20)"
    # left,right=str(edge).split(',')
    # print left[1:]
    # print (right[:-1])[1:]
    #
    # edges.append(edge)
    # edge = "(10, 30)"
    # left,right=str(edge).split(',')
    # print left[1:]
    # print (right[:-1])[1:]
    #
    # edges.append(edge)
    # edge = "(2, 3)"
    # left,right=str(edge).split(',')
    # print left[1:]
    # print (right[:-1])[1:]
    #
    # edges.append(edge)

    # print edges

    # while edge != 0:
    #     if edge not in edges:
    #         edges.append(edge)
        # edge = input("Enter edge number: ")



    return 1

def generateNodesMode():
    i = 0
    for edge in list(forward_edges):
        x = randomX()
        if x <= p:
            # print i,":",edge, "is up"
            forward_edges[i] = (edge[0], edge[1], 1)
            backward_edges[i] = (edge[1], edge[0], 1)
            # print forward_edges[i], " - ", backward_edges[i]
            # edge[3]="up"
        else:
            # print edge, " is down"
            forward_edges[i] = (edge[0], edge[1], 0)
            backward_edges[i] = (edge[1], edge[0], 0)
            # print forward_edges[i]," - ", backward_edges[i]
        i += 1
    global edges
    edges = forward_edges + backward_edges

def runWithM(M,terminal_pairs):
    r=0
    for i in range(M):
        # print "iteration: ",i+1
        generateNodesMode()
        all_terminal_connectivity=True
        for pair in terminal_pairs:
            if is2PointsConnected(pair[0],pair[1]) is False:
                # print pair[0],",", pair[1], "are not connected"
                all_terminal_connectivity=False
                break
            else:
                continue
        if all_terminal_connectivity is True:
            # print "all terminals are connected!\n"
            r+=1
        # else:
        #     print "not all terminals are connected\n"
    return r

def main():
    getNodes()
    getEdges()

    # generate terminal pairs
    terminal_pairs = [(terminals[i], terminals[j]) for i in range(len(terminals)) for j in range(i + 1, len(terminals))]
    terminal_pairs = terminal_pairs + [(terminals[j], terminals[i]) for i in range(len(terminals)) for j in range(i + 1, len(terminals))]
    # print terminal_pairs

    # print edges

    print "p\t\tM=1000\t\tM=10000\t"
    for prob in p_list:
        global p
        p=prob
        M=1000
        M2=10000
        print prob,"\t\t", runWithM(M,terminal_pairs)/1000.0,"\t\t",         runWithM(M2,terminal_pairs)/10000.0


def is2PointsConnected(a,b):
    graph = Graph(edges)
    result = graph.dijkstra(a, b)
    if len(result)==0:
        # print "no path"
        return False
    else:
        # print "path find: ", result
        return True


if __name__ == '__main__':
    main()




    # test()