# Importando algunas librerías que utilizaremos
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Pedir al usuario que ingrese el número de filas que desea
num_filas = int(input("Ingrese el número de conexiones: "))

# Crear un array de 4x4(filas columnas) con tipo de datos 'object'
array = np.empty((num_filas, 3), dtype='object')

# Pedir al usuario que ingrese los valores para cada elemento del array
for i in range(num_filas):
    array[i][0] = input("Ingresa el Origen: ")
    array[i][1] = input("Ingresa el Destino: ")
    array[i][2] = input("Ingresa el Peso: ")

# Crear un grafo no dirigido vacío
grafo = nx.Graph()
# Crear un grafo dirigido para dijkstra
subgrafo = nx.DiGraph()


###############     Agregar los nodos al grafo      ################################## 

### Nodos de origen
origenes = set([fila[0] for fila in array])#Recorro el array fila por fila y seleciono los datos de la primer columna
#Al utilizar set() sobre esa lista, se eliminan los valores duplicados y 
#se crea un conjunto con todos los nodos de origen únicos.
### Nodos de destino
destinos = set([fila[1] for fila in array])
#Se crean dos conjuntos, uno para los nodos de origen 
#y otro para los nodos de destino. Luego se unen en un 
#conjunto, que es lo que se agrega al grafo 
#utilizando el método add_nodes_from()
# gracias a esto se agregan todos los nodos
# a los grafos.
nodos = origenes.union(destinos)
grafo.add_nodes_from(nodos)


##################       Agregar las conexiones    ####################################### 

#En esta sección se agregan los bordes o conexiones al 
#grafo. Se recorre el array y se toman los valores del 
#origen, destino y peso para agregarlos al grafo 
#mediante el método add_edge().
for fila in array:
    origen = fila[0]
    destino = fila[1]
    peso = int(fila[2])
    grafo.add_edge(origen, destino, peso=peso)

# Obtener los pesos de las conexiones
pesos = nx.get_edge_attributes(grafo, 'peso')

# Dibujar el grafo con los pesos de las conexiones
nx.draw(grafo, pos=nx.spectral_layout(grafo), with_labels=True, node_size=500, font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(grafo, pos=nx.spectral_layout(grafo), edge_labels=pesos)


#DIJKSTRA


dij = list(nx.dijkstra_path(grafo, source=input("¿Cual es el nodo de origen?"), target=input("¿Cual es el nodo de Destino?"), weight='peso'))
print(dij)

subgrafo.add_nodes_from(dij)
#creo los pares de nodos para poder utilizar add_edges para generar el nuevo grafo
pares_nodos = [(dij[i], dij[i+1]) for i in range(len(dij)-1)]
pos = {pares_nodos[i]:[1,i] for i in range(len(pares_nodos)-1)}
subgrafo.add_edges_from(pares_nodos)
fig, ax = plt.subplots(figsize=(8,2))
nx.draw(subgrafo, with_labels=True, ax=ax)
