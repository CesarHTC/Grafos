import networkx as nx
import matplotlib.pyplot as plt

def prim(G):
    n = len(G)
    visited = [False] * n
    mst = [None] * n
    key = [float('inf')] * n
    key[0] = 0
    for i in range(n):
        u = min_key(key, visited)
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v] and G[u][v] < key[v]:
                mst[v] = u
                key[v] = G[u][v]
    return mst[1:]

def min_key(key, visited):
    min_val = float('inf')
    min_idx = -1
    for i in range(len(key)):
        if not visited[i] and key[i] < min_val:
            min_val = key[i]
            min_idx = i
    return min_idx


# Grafo de ejemplo como lista de aristas
G = [["A", "B", 20], ["A", "C", 7], ["B", "C", 15], ["B", "D", 15], ["C", "D", 25], ["C", "E", 6], ["D", "E", 4], ["C", "F", 7], ["F", "A", 6], ["F", "G", 4], ["G", "E", 20], ["G", "H", 6], ["H", "B", 12]]

# Encontrar los nodos únicos en el grafo
Origen = set([fila[0] for fila in G])
Destino = set([fila[1] for fila in G])
nodos = Origen.union(Destino)
nodos= list(nodos)
nodos.sort() 

# Crear matriz de adyacencia
matriz = [[float('inf')] * len(nodos) for i in range(len(nodos))]

# Llenar la matriz de adyacencia con los pesos de las aristas
for Origen, Destino, Peso in G:
    i = list(nodos).index(Origen)
    j = list(nodos).index(Destino)
    matriz[i][j] = Peso
    matriz[j][i] = Peso

    
mst = prim(G)

# Imprimir el Árbol Parcial Mínimo
print("Árbol Parcial Mínimo:")
for i in range(len(mst)):
    print(f"{mst[i]} - {i+1}")
