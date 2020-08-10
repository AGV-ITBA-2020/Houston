#https://networkx.github.io/
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mc

def gen_color(G):
    colors = []
    for n in G:
        d=nx.get_node_attributes(G,'description')[n]
        if d == "Station":
            colors.append(mc.to_rgba('red'))
        elif d == "Slow down Tag":
            colors.append(mc.to_rgba('green'))
        else:
            colors.append(mc.to_rgba('gray'))
    return colors

G=nx.DiGraph()

# adding just one node:
G.add_nodes_from([1,4,5,6], description="Station")
G.add_node(2, description="Slow down Tag")
G.add_node(3, description="Bifurcation", merge_to_node=2)

G.add_edge(1, 2, length=10 )
G.add_edge(2, 3, length=5 )
G.add_edge(3, 4, length=10 )
G.add_edge(3, 5, length=10 )
G.add_edge(4, 6, length=17 )
G.add_edge(5, 6, length=10 )

pos = {1:(0,0),2:(10,0),3:(20,0),4:(30,10),5:(30,-10), 6:(40,-10)}

#col=mc.to_rgba('red')
#nx.draw(G, with_labels=True, pos =pos)

#print(nx.shortest_path(G, source=1, target=6,weight="length"))

im = plt.imread("AGV.png")

nx.draw_networkx(G, with_labels=True, pos =pos,node_color=gen_color(G))
implot = plt.imshow(im, extent=[1,9,-5,5])
#plt.plot([0,25],[0,15])
plt.xlim((-5,45))
plt.ylim((-15,15))
plt.savefig("Map.png") # save as png
plt.show() # display



