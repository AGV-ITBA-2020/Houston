import networkx as nx
import matplotlib.colors as mc

class MapManager():
    def __init__(self):
        self.load_graph()
        self.draw_system()

    def load_graph(self):
        self.G = nx.DiGraph()
        self.G.add_nodes_from([1, 4, 5, 6], description="Station")
        self.G.add_node(2, description="Slow down tag")
        self.G.add_node(3, description="Bifurcation", merge_node=2, fork_left_node=4)

        self.G.add_edge(1, 2, length=10)
        self.G.add_edge(2, 3, length=5)
        self.G.add_edge(3, 4, length=10)
        self.G.add_edge(3, 5, length=10)
        self.G.add_edge(4, 6, length=17)
        self.G.add_edge(5, 6, length=10)

        self.pos = {1: (0, 0), 2: (10, 0), 3: (20, 0), 4: (30, 10), 5: (30, -10), 6: (40, -10)}

    def get_path(self,orig,dest):
        node_path=nx.shortest_path(self.G, source=orig, target=dest,weight="length")
        descr=nx.get_node_attributes(self.G, 'description')
        merge2node = nx.get_node_attributes(self.G, 'merge_node')
        forkleftnode = nx.get_node_attributes(self.G, 'fork_left_node')
        strOut=""
        for i in range(len(node_path)): ###Falta revisar
            curr_node=node_path[i]
            if i!=0: #El primer punto es omitido en el mensaje
                if descr[curr_node] == "Station":
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
        return strOut

    def draw_system(self):
        nx.draw_networkx(self.G, with_labels=True, pos=self.pos, node_color=self.gen_color())
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