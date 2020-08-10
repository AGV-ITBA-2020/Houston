#https://networkx.github.io/
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mc

G=nx.Graph()

# adding just one node:
G.add_nodes_from([1,4,5], description="Station")
G.add_node(2, description="Slow down Tag")
G.add_node(3, description="Merge to: 2")

G.add_edge(1, 2, weight=10 )
G.add_edge(2, 3, weight=5 )
G.add_edge(3, 4, weight=5 )
G.add_edge(3, 5, weight=10 )

pos = {1:(0,0),2:(10,0),3:(20,0),4:(30,10),5:(30,-10)}

col=mc.to_rgba('red')

#nx.draw(G, with_labels=True, pos =pos)
nx.draw_networkx(G, with_labels=True, pos =pos,node_color=col)
plt.savefig("Map.png") # save as png
plt.show() # display