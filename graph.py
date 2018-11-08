# The first step towards any graph problem is to construct one 

# define a Vertex class , in which it contains all the necessary attributes about a node such as , its neighbours , the weight of the the edges 
# Using dictionary is probably the easiest ------ mimic the adjacency list representaion of graphs 

class Vertex:
    def __init__(self, node_name):
        self.id = node_name 
        #using dictionary to store all the neighbours of a node 
        self.adjacent = {}
        self.parent = None
        self.visited = False
    
    #return the name of the node 
    def get_id(self):
        return self.id
    #adding a neighbour -----> we want the neighbour to be a vertex object as well
    # so that we can use methods defined in this class on them
    def add_neighbour (self, neighbour_vertex, edge_weight = 0):
        self.adjacent[neighbour_vertex] = edge_weight
    
    #returning all neighbours given a node 
    def get_neighbours(self):
        return self.adjacent.keys()
    #return the edge_weight between this node and a neighbour 
    def get_weight(self,neighbour):
        return self.adjacent[neighbour]
    #a useful function to assign a parent to this node 
    def set_parent(self,parent_node):
        self.parent = parent_node
    
    # when we want to print out a Vertex object , we have to define a __str__ method, then when we call print(Node) , it will print in the way
    # defined in this function 
    def __str__(self):
        #print the node id and all of its neighbours 
        return str(self.id) + "adjacent nodes :" + str ([x.id for x in self.adjacent])

# Now we have a basic class for Nodes , we need another class to contruct the grapgh 

class Graph:
    #a graph should contain a dictionary of Vertex objects
    def __init__(self):
        self.vertex_dict = {}
        self.num_vertices = 0
    #define iterator function , so that when we iterating a graph objects. Since the key value in graph object is the name 
    # of a node, but we want to iterate the actual Vertx object 
    def __iter__(self):
        return iter(self.vertex_dict.values())
    
    # the most basic method should be adding a node 
    def add_node(self, node):
        self.num_vertices += 1
        new_vertext = Vertex(node)
        self.vertex_dict[node] = new_vertext
    # adding edges 
    def add_edge(self, source, end, weight=  0):
        #check is bouth source and end are in the graph, if not add them first 
        if source not in self.vertex_dict:
            self.add_node(source)
        if end not in self.vertex_dict:
            self.add_node(end)
        
        # an edge is of form (a,b), in adjaceny list representaion , an edge is stored twice
        # that is a is in neighbours of b and b is in neighbours of a 
        self.vertex_dict[source].add_neighbour(self.vertex_dict[end],weight)
        self.vertex_dict[end].add_neighbour(self.vertex_dict[source],weight)
    
    # returning all vertices 
    def get_vertices (self):
        return self.vertex_dict.keys()
    
    # check if a node is in our graph 
    def get_node (self, node):
        if node in self.vertex_dict.keys():
            return node 
        else :
            return None



def BFS (aGraph, source_node):
    # initialize a new graph object for all the nodes that are reachable from the source node 
    connected_ = Graph()
    # initialize the L[0] to contain the source node id 
    # the Layer counter starts at 0
    layer_count = 0
    L = [[]] 
    # first layer , only the source node object  
    L[0].append(aGraph.vertex_dict[source_node])
    
    # while the BFS found another layer that is connected
    while L[layer_count] != [] :
        # initialze empty list for L[i+1]
        L.append([])
        # for every node that is in L[i]
        for u in L[layer_count]:
            # consider each edge (u,v) that is incident to u 
            for e in u.get_neighbours():
                if e.visited == False :
                    # set visited to be true 
                    e.visited = True 
                    connected_.add_node(e.get_id()) 
                    L[layer_count + 1].append(e)
        layer_count = layer_count + 1
    return connected_    

         

places = [  ["Toronto", "New york"],
            ["Toronto", "Ottawa"],
            ["Montreal", "Chicago"],
            ["New york", "Boston"],
            ["Boston", "florida"],
            ["Boston", "texas"]
         ]

g2 = Graph()
for i in places :
    for j in i :
        if g2.get_node(j) == None :
            g2.add_node(j)
        g2.add_edge(i[0],i[1])

print("all nodes in this graph are")
for e in g2:
    print(e.get_id())
print('\n')


print("all neighbours of Toronto are")

for e in g2.vertex_dict['Toronto'].get_neighbours():
    print (e.get_id())

connected_path = BFS(g2,'Toronto')

print("\n")

print("all cities accessble node Toronto are")
for e in connected_path:
    print(e.get_id() )

print("\n")





'''

g = Graph()

g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')
g.add_node('f')
g.add_edge('a', 'b', 7)  
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

path = BFS(g,'a')
print("all nodes accessable from node a are")
for e in path:
    print(e.get_id() )

print("\n")


for e in g:
    print(e.get_id())

print("all neighbours of vertex a are")

for e in g.vertex_dict['a'].get_neighbours():
    print (e.get_id())

#print(g.vertex_dict['a'].get_neighbours())


'''




'''
a = {}
a['a'] = 1
a['b'] = 4
a['c'] = 5

for e in iter(a.values()) :
    print(e)
'''