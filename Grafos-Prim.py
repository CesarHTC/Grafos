import networkx as nx
import matplotlib.pyplot as plt

# Grafo de ejemplo
G = [["A", "B", 20], ["A", "C", 7], ["B", "C", 15], ["B", "D", 15], ["C", "D", 25], ["C", "E", 6], ["D", "E", 4], ["C", "F", 7], ["F", "A", 6], ["F", "G", 4], ["G", "E", 20], ["G", "H", 6], ["H", "B", 12]]

# Crear grafo de NetworkX
G_nx = nx.Graph()
for Origen, Destino, Peso in G:
    G_nx.add_edge(Origen, Destino, weight=Peso)
#Arbol minimo de  
T = nx.minimum_spanning_tree(G_nx)

# Visualizar el grafo 
pos = nx.circular_layout(G_nx)



nx.draw_networkx(G_nx, pos, with_labels=True)
labels = nx.get_edge_attributes(G_nx, 'weight')
nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=labels)
plt.title("Grafo Original")
plt.show()
# Visualizar el árbol parcial mínimo

nx.draw_networkx(T, pos, with_labels=True)
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
plt.title("Árbol Parcial Mínimo")


plt.show()
