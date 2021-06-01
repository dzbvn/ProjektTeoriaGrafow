import numpy as np

class Edge:
    v1 = ''
    v2 = ''
    w = 0
    def __init__(self, _v1, _v2, _w = 0):
        self.v1 = _v1
        self.v2 = _v2
        self.w = _w

class Graph:
    Edges = []
    Vertices = set()

    Distances = []
    PreviousV = []

    Txt = str()

    def readGraph(self, txt):
        self.Txt = txt
        lines = txt.split('\n')

        if '' in lines:
            lines.remove('')

        for line in lines:

            tline = replaceA(line)

            if tline == '':
                continue
            self.Vertices.add(tline[0])

            c = 1
            while c != len(tline):
                if tline[c+1] == "-":
                    self.Vertices.add(tline[c])
                    self.Edges.append(Edge(tline[0], tline[c], int(tline[c + 1] + tline[c+2])))
                    c += 1
                else:
                    self.Vertices.add(tline[c])
                    self.Edges.append(Edge(tline[0], tline[c], int(tline[c + 1])))

                c += 2
        #for edge in self.Edges:
        #    print(edge.v1, edge.v2, edge.w)

    def printGraph(self):
        print(self.Txt)
        print("")


    def bellmanFord(self, src):
        dist = dict()
        prev = dict()

        for i in self.Vertices:
            dist[i] = np.inf

        dist[src] = 0
        prev[src] = '-'

        for v in range(len(self.Vertices)):

            for edge in self.Edges:
                #print(edge.v1, "    ", edge.v2)
                #print(dist[edge.v1],"+", edge.w,"<", dist[edge.v2])
                if dist[edge.v1] + edge.w < dist[edge.v2]:
                    dist[edge.v2] = dist[edge.v1] + edge.w
                    #print(edge.v2, "=" , dist[edge.v1]+edge.w)
                    prev[edge.v2] = edge.v1
            #print(dist)
            #print(prev)

        for edge in self.Edges:
             if dist[edge.v1] != np.inf and dist[edge.v1] + edge.w < dist[edge.v2]:
                 return 1

        self.Distances = dist
        self.PreviousV = prev

    def printResult(self):
        print("| V | ", end='')
        for v in range(len(self.Vertices)):
            print(chr(65+v), end=' | ')
        print("")

        print("| d | ", end='')
        for v in range(len(self.Vertices)):
            print(self.Distances[chr(65+v)], end=' | ')
        print("")

        print("| p | ", end='')
        for v in range(len(self.Vertices)):
            print(self.PreviousV[chr(65 + v)], end=' | ')
        print("")

    def clear(self):
        self.Edges.clear()
        self.Vertices.clear()

        self.Distances.clear()
        self.PreviousV.clear()


def replaceA(line):
    dic = { "[": "", "]": "", " ": "", "=": "", ">": "", "\n": ""}
    for i, j in dic.items():
        line = line.replace(i, j)
    return line

def readFile(filename):

    with open(filename) as file:
        text = file.read()
    res = text.split(',')

    return res

if __name__ == '__main__':

    listOfGraphs = readFile("graph1.txt")
    graphs = []
    i = 0

    for i, graphTxt in enumerate(listOfGraphs):
        graph = Graph()

        graph.clear()
        graph.readGraph(graphTxt)

        if(graph.bellmanFord('A') == 1):
            print("Negative weight cycle")
        graph.printGraph()
        graph.printResult()

