


class Edge:
    def __init__(self, n1, n2):
        self.nodes = (n1, n2)
    
    def contains(self, n):
        return n in self.nodes
    
    def get_child(self, n):
        if n == self.nodes[0]:
            return self.nodes[1]
        elif n == self.nodes[1]:
            return self.nodes[0]
        else:
            return None
        
    def directed_equal(self, e):
        return self.nodes == e.nodes
    
    def undirected_equal(self, e):
        return self.nodes == e.nodes or (self.nodes[1] == e.nodes[0] and self.nodes[0] == e.nodes[1])


class Graph:
    def __init__(self):
        self.edges = []
        
    def create_graph(self, graph):
        for k, v in graph.items():
            for n in v:
                self.connect(k, n)
        
    def get_children(self, n):
        children = []
        for edge in self.edges:
            if edge.contains(n) and edge.get_child(n) not in children:
                children.append(edge.get_child(n))
        return children
    
    def connect(self, n1, n2):
        e = Edge(n1, n2)
        e_temp = Edge(n2, n1)
        if e not in self.edges and e_temp not in self.edges:
            self.edges.append(e)
            
    def iter_dfs(self, start, limit, goal = None):
        visited = []
        stack = [(start, 0)]
        level = 0
        while stack:
            node, level= stack.pop()
            if node in visited:
                continue
            
            visited.append(node)
            children = self.get_children(node)
            
            #for goal 
            if goal != None:
                if node == goal:
                    print("Goal reached")
                    return visited
                
            
            added = False
            if level < limit:
                children.reverse()
                for child in children:
                    if child not in visited:
                        added = True
                        stack.append((child, level + 1))
                if added:
                    level += 1
                else:
                    level -= 1
        if goal != None:            
            print("Goal not reached")
        return visited
    
    def getDis(self, n):
        citiesWithSLDistance = [('Arad', 366), ('Bucharest', 0), ('Craivoa', 160), ('Dobreta', 242), ('Eforie', 161), ('Fagaras', 178), ('Giurgiu', 77), ('Hirsova', 151), ('Iasi', 226), ('Lugoj', 244), ('Mehadia', 241), ('Neamt', 234), ('Oradea', 380), ('Pitesti', 98), ('Rimnicu Vilcea', 193), ('Sibiu', 253), ('Timisoara', 329), ('Urziceni', 80), ('Vaslui', 199), ('Zerind', 374)]
        for i in citiesWithSLDistance:
            if i[0] == n:
                return i[1]
    
    def gbfs(self, start, end):
        visited = []
        queue = [(start, self.getDis(start))]
        while queue:
            node, h = queue.pop(0)
            if node not in visited:
                visited += [node]
                if node == end:
                    break
                for child in self.get_children(node):
                    if child[0] not in visited:
                        queue += [(child[0], self.getDis(child[0]))]
                        
                
                queue.sort(key = lambda queue: queue[1])
        return visited
    
    def astar(self, start, end):
        visited = []
        queue = [(start, 0, self.getDis(start), 0)]
        while queue:
            node, dis, h, temp = queue.pop(0)
            if node not in visited:
                visited += [node]
                if node == end:
                    break
                for child in self.get_children(node):
                    if child[0] not in visited:
                        queue += [(child[0], child[1] + dis, self.getDis(child[0]), child[1])]
                queue.sort(key = lambda queue: queue[1]+queue[2])
                print(queue)
        return visited
                        

global citiesWithSLDistance
citiesWithSLDistance = [('Arad', 366), ('Bucharest', 0), ('Craivoa', 160), ('Dobreta', 242), ('Eforie', 161), ('Fagaras', 178), ('Giurgiu', 77), ('Hirsova', 151), ('Iasi', 226), ('Lugoj', 244), ('Mehadia', 241), ('Neamt', 234), ('Oradea', 380), ('Pitesti', 98), ('Rimnicu Vilcea', 193), ('Sibiu', 253), ('Timisoara', 329), ('Urziceni', 80), ('Vaslui', 199), ('Zerind', 374)]


def getDis(n):
    for i in citiesWithSLDistance:
        if i[0] == n:
            return i[1]
        
        
cityGraph = {
'Arad':[('Zerind', 75),('Sibiu', 140),('Timisoara', 118)],
'Bucharest':[('Fagaras', 211), ('Pitesti', 101),('Urziceni', 85),('Giurgiu', 90)],
'Craivoa':[('Rimnicu Vilcea', 146),('Pitesti', 138),('Dobreta', 120)],
'Dobreta':[('Mehadia', 75),('Craivoa', 120)],
'Eforie':[],
'Fagaras':[('Sibiu', 90),('Bucharest', 211)],
'Giurgiu':[],
'Hirsova':[('Urziceni', 98),('Eforie', 86)],
'Iasi':[('Neamt', 87), ('Vaslui', 92)],
'Lugoj':[('Timisoara', 111),('Mehadia', 70)],
'Mehadia':[('Lugoj', 70),('Dobreta', 75)],
'Neamt':[],
'Oradea':[('Zerind', 71),('Sibiu', 151)],
'Pitesti':[('Rimnicu Vilcea', 97),('Bucharest', 101),('Craivoa', 138)],
'Rimnicu Vilcea':[('Sibiu', 80),('Pitesti', 97),('Craivoa', 146)],
'Sibiu':[('Oradea', 151),('Arad', 140),('Fagaras', 99),('Rimnicu Vilcea', 80)],
'Timisoara':[('Arad', 118),('Lugoj', 111)],
'Urziceni':[('Vaslui', 142),('Hirsova', 98),('Bucharest', 85)],
'Vaslui':[('Iasi', 92),('Urziceni', 142)],
'Zerind':[('Oradea', 71),('Arad', 75)]
}

g = Graph()
g.create_graph(cityGraph)

start = "Arad"
end = "Bucharest"
print("Path from {} to {} using Greedy Best First Search:".format(start, end))
print(g.gbfs(start, end))

print("\n\n")
start = "Arad"
end = "Bucharest"
print("Path from {} to {} using A Star Search:".format(start, end))
print(g.astar(start, end))
print("\n\n")