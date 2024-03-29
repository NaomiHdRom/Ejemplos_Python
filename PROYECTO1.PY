#Ejemplo obtenido de videos de Youtube: https://www.youtube.com/watch?v=rldKl1CNx-A&list=PLGZqdNxqKzfYXTwYAZIlmjnQmrytCSR1J&index=1

import networkx as nx 
import matplotlib.pyplot as plt
import numpy as np
import random


G=nx.Graph() #Se genera el gráfico

G.add_nodes_from(["A",
                  "B",
                  "C",
                  "D",
                  "E"])


position={           #Se hace una libreria que contiene la ubicacion que deseamos en el mapa (x,y)
    "A":(1,5),
    "B":(4.5,6.6),
    "C":(5.6,6),
    "D":(3,4),
    "E":(6,2)
    
}


G.add_edges_from([
    ("A", "C",{"distancia": 1}),  # Se añaden las uniones con sus atributos
    ("B", "C", {"distancia":0.5})
      
    #Para acceder al dato y usarlo mas adelante en codigo G.nodes["A"] o G.edges["A"]
])


for edge in G.edges(data=True):
    print(edge)
    
edge_labels={(u,v):d["distancia"]for u,v,d in G.edges(data=True)}
    

nx.draw(G,pos=position,with_labels=True,
        node_color="red", node_size=3000, 
        font_color="white",font_size=20, 
        font_family="Times New Roman", 
        font_weight="bold", width=5)

nx.draw_networkx_edge_labels(G,pos=position,edge_labels=edge_labels,
                            label_pos=0.5
                             )


plt.margins(0.2)


plt.show()