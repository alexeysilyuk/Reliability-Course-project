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
edges={"1,2":"down",
       "1,3":"down",
       "2,3":"down",}


edges2=[("1", "2", 0), ("2", "3", 0), ("2", "4", 0)
        # , ("b", "c", 0),
        # ("b", "d", 0), ("c", "d", 0), ("c", "f", 0), ("d", "e", 0),
        # ("e", "f", 0)
        ]
r=0
p=0.9
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
    for edge in list(edges2):
        print i

        x = randomX()
        if x <= p:
            print edge, "is up"
            edges2[i]=(edge[0],edge[1],1)
            # edge[3]="up"
        else:
            print edge, " is down"
            print
            edges2[i]=(edge[0],edge[1],0)

        i += 1
    print edges2

def is2PointsConnected(a,b):
    graph = Graph(edges2)

    print(graph.dijkstra("1", "4"))




if __name__ == '__main__':
    main()
    is2PointsConnected(1,2)
    # test()