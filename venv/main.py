import random
from collections import deque, namedtuple

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
                # if(cost==0):
                #     break
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
edges={"1,2":"down",
       "1,3":"down",
       "2,3":"down",}

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

edges2=[]
r=0
p=0.7
x=0


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


def main():
    getNodes()
    getEdges()
    i=0
    for edge in list(forward_edges):
        x = randomX()
        if x <= p:
            # print i,":",edge, "is up"
            forward_edges[i]=(edge[0],edge[1],1)
            backward_edges[i] = (edge[1], edge[0], 1)
            print forward_edges[i]," - ", backward_edges[i]
            # edge[3]="up"
        else:
            # print edge, " is down"
            forward_edges[i]=(edge[0],edge[1],9999)
            backward_edges[i] = (edge[1], edge[0], 9999)
            print forward_edges[i]," - ", backward_edges[i]
        i += 1
    global edges2
    edges2=forward_edges+backward_edges
    print edges2

def is2PointsConnected(a,b):
    graph = Graph(edges2)

    print(graph.dijkstra(a, b))




if __name__ == '__main__':
    main()
    is2PointsConnected('17','1')
    # test()