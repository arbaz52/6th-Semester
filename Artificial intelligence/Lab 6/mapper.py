# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 10:10:35 2019

@author: Shark
"""

graph = {'Arad': [('Zerind', 75, 374), ('Sibiu', 140, 253), ('Timisoara', 118, 329)], 'Bucharest': [('Fagaras', 211, 178), ('Pitesti', 101, 98), ('Urziceni', 85, 80), ('Giurgiu', 90, 77)], 'Craivoa': [('Rimnicu Vilcea', 146, 193), ('Pitesti', 138, 98), ('Dobreta', 120, 242)], 'Dobreta': [('Mehadia', 75, 241), ('Craivoa', 120, 160)], 'Eforie': [], 'Fagaras': [('Sibiu', 90, 253), ('Bucharest', 211, 0)], 'Giurgiu': [], 'Hirsova': [('Urziceni', 98, 80), ('Eforie', 86, 161)], 'Iasi': [('Neamt', 87, 234), ('Vaslui', 92, 199)], 'Lugoj': [('Timisoara', 111, 329), ('Mehadia', 70, 241)], 'Mehadia': [('Lugoj', 70, 244), ('Dobreta', 75, 242)], 'Neamt': [], 'Oradea': [('Zerind', 71, 374), ('Sibiu', 151, 253)], 'Pitesti': [('Rimnicu Vilcea', 97, 193), ('Bucharest', 101, 0), ('Craivoa', 138, 160)], 'Rimnicu Vilcea': [('Sibiu', 80, 253), ('Pitesti', 97, 98), ('Craivoa', 146, 160)], 'Sibiu': [('Oradea', 151, 380), ('Arad', 140, 366), ('Fagaras', 99, 178), ('Rimnicu Vilcea', 80, 193)], 'Timisoara': [('Arad', 118, 366), ('Lugoj', 111, 244)], 'Urziceni': [('Vaslui', 142, 199), ('Hirsova', 98, 151), ('Bucharest', 85, 0)], 'Vaslui': [('Iasi', 92, 226), ('Urziceni', 142, 80)], 'Zerind': [('Oradea', 71, 380), ('Arad', 75, 366)]}
def get_sld(graph, name):
    for k, children_arr in graph.items():
        for child in children_arr:
            if child[0] == name:
                return child[2]
            
def astar(graph, start, end):
    visited = []
    queue = [(start, 0, get_sld(graph, start))]
    while queue:
        name, dist, sld = queue.pop(0)
        if name not in visited:
            visited.append(name)
            if name == end:
                break
            children = graph[name]
            for child in children:
                queue.append((child[0], child[1] + dist, child[2]))
            queue.sort(key = lambda queue: queue[1] + queue[2])
            
    return visited
    
print(astar(graph, "Arad", "Bucharest"))