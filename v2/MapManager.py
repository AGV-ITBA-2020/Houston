import networkx as nx
import matplotlib.colors as mc
import matplotlib.pyplot as plt

class MapManager():
    def __init__(self):
        self.load_graph()

        self.agv_im_w = 8 #Tamaño imagen AGV
        self.agv_im_h = 5
        self.agv_pos_list={}
        self.agv_im = plt.imread("AGV.png")

        # self.draw_system()

    def load_graph(self): ##Acá se genera el grafo a mano. Se podría poner en un archivo y luego cargarlo, sería más modular
        self.G = nx.DiGraph()
        self.G.add_nodes_from([1, 3, 5], description="Station") #Nodos estación
        self.G.add_node(2, description="Bifurcation", merge_node=5, fork_left_node=4) #Bifurcación: merge_node es al que mergea, y el fork left es 4
        self.G.add_node(4, description="Bifurcation", merge_node=1,fork_left_node=3)  # Bifurcación: merge_node es al que mergea, y el fork left es 4
        #Vértices entre nodos con sus respectivas distancias
        self.G.add_edge(1, 5, length=140)
        self.G.add_edge(5, 2, length=100)
        self.G.add_edge(2, 3, length=265)
        self.G.add_edge(3, 4, length=380)
        self.G.add_edge(2, 4, length=250)
        self.G.add_edge(4, 1, length=110)
        #Posiciones de los nodos gráficamente (hecho a manopla)
        self.pos = {1: (-4, 0), 2: (8, 6), 3: (0, 20), 4: (-8, 6),5: (4, 0)}
        # self.xlimDefault = (-12,12) # Límites del plot por default
        # self.ylimDefault = (-5,22)
        # plt.xlim(self.xlimDefault )
        # plt.ylim(self.ylimDefault )

    def get_path(self,orig,dest): #Dado un origen y destino obtiene el mensaje en código que representa el camino, la lista de nodos por la que pasa y las distancias que recorre.
        node_path=nx.shortest_path(self.G, source=orig, target=dest,weight="length")
        dist_list = [] ##Vector donde se guardan las distancias como lista de strings
        descr=nx.get_node_attributes(self.G, 'description')
        merge2node = nx.get_node_attributes(self.G, 'merge_node')
        forkleftnode = nx.get_node_attributes(self.G, 'fork_left_node')
        strOut=""
        for i in range(len(node_path)): #Para cada nodo en el camino
            curr_node=node_path[i]
            if i!=0: #El primer punto es omitido en el mensaje
                dist_list.append(str(self.G.edges[node_path[i-1], curr_node]['length'])) ## Pusheo la distancia que hay al anterior nodo
                if descr[curr_node] == "Station": #Dependiendo del tipo de nodo agrego el objetivo que pretendo
                    strOut += "St"
                elif descr[curr_node] == "Slow down tag":
                    strOut += "Sd"
                elif descr[curr_node] == "Speed up tag":
                    strOut += "Su"
                elif descr[curr_node] == "Bifurcation":
                    if node_path[i-1] == merge2node[curr_node]: #Viene del camino al que se va a dividir
                        if forkleftnode[curr_node] == node_path[i+1]:
                            strOut += "Fl"
                        else:
                            strOut += "Fr"
                    else:
                        strOut += "Me" #merge
        return strOut, node_path, dist_list

    # def draw_system(self):
        # self.xlim=plt.xlim()
        # self.ylim=plt.ylim()
        # plt.clf()
        # #nx.draw_networkx(self.G, with_labels=True, pos=self.pos, node_color=self.gen_color())
        # for key in self.agv_pos_list:
        #     node1 = self.agv_pos_list[key][0]
        #     node2 = self.agv_pos_list[key][1]
        #     if (node1 == node2):
        #         x_center = self.pos[node1][0]
        #         y_center = self.pos[node1][1]
        #     else:
        #         fracTrav = self.agv_pos_list[key][2] / self.G.edges[node1, node2]['length'] #Fracción del camino recorrido
        #         x_center = self.pos[node1][0] + (self.pos[node2][0] - self.pos[node1][0]) * fracTrav
        #         y_center = self.pos[node1][1] + (self.pos[node2][1] - self.pos[node1][1]) * fracTrav
        #     implot = plt.imshow(self.agv_im, extent=[x_center-self.agv_im_w/2, x_center+self.agv_im_w/2, y_center-self.agv_im_h/2, y_center+self.agv_im_h/2])
        # plt.xlim(self.xlim)
        # plt.ylim(self.ylim)
    def gen_color(self):
        colors = []
        for n in self.G:
            d = nx.get_node_attributes(self.G, 'description')[n]
            if d == "Station":
                colors.append(mc.to_rgba('red'))
            elif d == "Slow down tag":
                colors.append(mc.to_rgba('green'))
            else:
                colors.append(mc.to_rgba('gray'))
        return colors

    def update_agv_pos(self,agv_num,location_node, next_node,dist):
        self.agv_pos_list[agv_num] = [location_node,next_node,dist]
        #self.draw_system()
#Mapa viejo
# self.G.add_nodes_from([1, 4, 5, 6], description="Station") #Nodos estación
# self.G.add_node(2, description="Slow down tag") #Nodos de "tags"
# self.G.add_node(3, description="Bifurcation", merge_node=2, fork_left_node=4) #Bifurcación: merge_node es al que mergea, y el fork left es 4
# #Vértices entre nodos con sus respectivas distancias
# self.G.add_edge(1, 2, length=8)
# self.G.add_edge(2, 3, length=5)
# self.G.add_edge(3, 4, length=10)
# self.G.add_edge(3, 5, length=9)
# self.G.add_edge(4, 6, length=17)
# self.G.add_edge(5, 6, length=11)
# #Posiciones de los nodos gráficamente (hecho a manopla)
# self.pos = {1: (0, 0), 2: (10, 0), 3: (20, 0), 4: (30, 10), 5: (30, -10), 6: (40, -10)}
# self.xlimDefault = (-5,45) # Límites del plot por default
# self.ylimDefault = (-15,15)
# plt.xlim(self.xlimDefault )
# plt.ylim(self.ylimDefault )