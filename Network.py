# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:36:05 2020

@author: Christian
"""
import networkx as nx
import matplotlib.pyplot as plt
from random import randint

#LOG FILE
logFile = open('LogFile.txt',"w+")
logFile.write("\t\tLOG FILE START\n")


#Function defs

#This function is used during the initial network creation to insure each node starts with an edge
def initialNodeCreation(Paret,letterCount,nNodes):
        
    
    
    for i in range(len(letterCount)):
        
        buffer = randint(0,nNodes-1)
        #print("nNodes: " + str(nNodes) + " buffer: " + str(buffer))
        
        if letterCount[buffer] != 1:
            letterCount[buffer] = 1
            print(letterCount)
            return buffer
    print(letterCount)
    return randint(0,nNodes)

#Appendes all current edges to a log file 
def logEdgesAppend(fp,graph,step):
    
        fp.write("Step: " + str(step) + "\t\t-EDGES-\n")
        
        for edge in graph.edges.data():
            fp.write('\t' + str(edge) +'\n')




#Random number for node generation
numberOfNodes = randint(15,26)

#Create graph
Network = nx.Graph()
plt.figure(figsize = (10,10))

#Node names
nodeNames = ['A','B','C','D','E','F','G','H','I'
            ,'J','K','L','M','N','O','P','Q','R'
            ,'S','T','U','V','W','X','Y','Z']

#Creating network nodes
for i in range(numberOfNodes):
  Network.add_node(nodeNames[i])

#Give each node a random position
NodePos = nx.spring_layout(Network)

#Random number for edge generation
numberOfEdge = randint(20,25)

#Label the nodes
nx.draw_networkx_labels(Network, NodePos, font_size=20)



#Create initial network edges
letterCount = [0]*numberOfNodes
breakVal = 0
while breakVal != 1:
    parent = randint(0,numberOfNodes-1)
    Network.add_edge(nodeNames[parent] ,nodeNames[initialNodeCreation(parent,letterCount,numberOfNodes)] ,weight=randint(1,5))
    
    if 0 not in letterCount:
        breakVal = 1

#Visualize the nodes 
nx.draw_networkx_nodes(Network, NodePos, node_size=700, node_color='green')

#Visualize the edges
nx.draw_networkx_edges(Network, NodePos, width=2)

#Logging intial edges and nodes 

logEdgesAppend(logFile,Network,1)

logFile.close()

plt.axis("off")
plt.savefig('Test.png')
