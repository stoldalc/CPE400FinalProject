# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:36:05 2020

@author: Christian
"""
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

#LOG FILE
logFile = open('LogFile.txt',"w+")
logFile.write("\t\tLOG FILE START\n")
logFile.close()


#Function defs

#This function is used during the initial network creation to insure each node starts with an edge
def initialNodeCreation(Paret,letterCount,nNodes):
        
    
    
    for i in range(len(letterCount)):
        
        buffer = randint(0,nNodes-1)
        #print("nNodes: " + str(nNodes) + " buffer: " + str(buffer))
        
        if letterCount[buffer] != 1:
            letterCount[buffer] = 1
            #print(letterCount)
            return buffer
    #print(letterCount)
    return randint(0,nNodes)

#Appendes all current edges to a log file 
def logEdgesAppend(fp,graph,step):
    
        fp.write("Step: " + str(step) + "\t\t-EDGES-\n")
        
        for edge in graph.edges.data():
            fp.write('\t' + str(edge) +'\n')

#Function to remove nodes
def nodeFailure(g,n,step):
  print("\t Removing node: " + n)
  buffer = g.edges(n)
  
  logFile = open('LogFile.txt',"a+")
  logFile.write("Step: "  + str(step) + "\t\t-NODE REMOVAL-\n")
  logFile.write("\tNode: " + n + " removed\n")
  logFile.close()

  for tuple in list(buffer):
    g.remove_edge(tuple[0],tuple[1])
  buffer = g.edges(n)

  return g


#Function to remove edges
def linkFailure(g,n1,n2,num):

  print("\tRemoving the edge between: " + str(n1) + " and " + str(n2))
  logFile = open('LogFile.txt',"a+")
  logFile.write("Step: "  + str(num) + "\t\t-LINK REMOVAL-\n")
  logFile.write("\tEdge: " + str(n1) + "," + str(n2) + " removed\n")
  logFile.close()    

  g.remove_edge(n1,n2) 
  
  return g

#Returns a tuple representing a random edge
def randomEdge(g):
    edgesList = list(g.edges())
    
    buffer = edgesList[randint(0,len(edgesList))]
        
    return buffer

def findPath(g):
    nodesList = list(g.nodes())
    
    n1 = nodesList[randint(0,len(nodesList))]
    n2 = nodesList[randint(0,len(nodesList))]
    
    print("Attempting to find a path between: " + n1 + ' and ' + n2)
    
    return nx.dijkstra_path(g,n1,n2)

def edgeListCreation(l):
    #tuppleList = []
    
    '''
    for i in range(len(l-1)):
        buffer = []
        buffer.append[i]
        buffer.append[i+1]
        tuppleList.append(buffer)
    '''
    tuppleList = [(l[i],l[i+1]) for i in range(len(l)-1)]
    print("\tTupples list: " + str(tuppleList))
    return tuppleList
        
    
  
#updating the graph
def networkUpdate(num):
    ax.clear()
    logFile = open('LogFile.txt',"a+")
    
    global Network
    
    #Randomly select if a node or a link will fail
    if randint(0,1) == 1:
        print(str(num) + ": Node has randomly failed ")
        Network = nodeFailure(Network,nodeNames[randint(0,25)],num)
    else:
        print(str(num) + ": Link has randomly failed ")
        
        edgeBuffer = randomEdge(Network)
        Network = linkFailure(Network,edgeBuffer[0],edgeBuffer[1],num)
    
    
    #Label the nodes
    nx.draw_networkx_labels(Network, NodePos, font_size=20)

    #Visualize the nodes 
    nx.draw_networkx_nodes(Network, NodePos, node_size=700, node_color='green')
    
    #select 2 nandom nodes to send a packet between
    shortestPath = findPath(Network)
    shortestPathEdges = edgeListCreation(shortestPath)
    #print("Shortest path: " + str(edgeListCreation(shortestPath)))
    

    #Visualize the edges
    
    nx.draw_networkx_edges(Network, NodePos, width=.5, edge_color = 'black')
    nx.draw_networkx_edges(Network, NodePos, shortestPathEdges, width=2, edge_color = 'green')
    
    #nx.draw(Network, NodePos)

    #fig, ax = plt.subplots(figsize=(10, 10))

    #Logging current status of edges and nodes
    print(str(num) + ": loging edges")
    logEdgesAppend(logFile,Network,num)
    
    
    
    
    logFile.close()
    
    #plt.axis("off")
    return Network




#Random number for node generation
numberOfNodes = randint(15,26)

#Create graph
Network = nx.Graph()
#plt.figure(figsize = (10,10))

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
#logFile = open('LogFile.txt',"a+")
#logEdgesAppend(logFile,Network,1)
#logFile.close()

#Build the intial plt
fig, ax = plt.subplots(figsize=(10, 10))

plt.axis("off")
#plt.savefig('Test.png')



'''
************Testing***************
'''

animationLength = 9000
#plt.figure(figsize = (10,10))
'''
animation = matplotlib.animation.FuncAnimation(fig,
                                               networkUpdate, 
                                               frames = 30,
                                               interval = 10000, 
                                               repeat = True)
'''

animation = animation.FuncAnimation(fig, networkUpdate, frames=20, interval=1000, repeat = False)
plt.show()

#plt.savefig('Test1.gif')

