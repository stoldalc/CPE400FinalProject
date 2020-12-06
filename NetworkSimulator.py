# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:36:05 2020

@author: Christian
"""
import networkx as nx
#import matplotlib
#matplotlib.use("Agg")
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
        
        if letterCount[buffer] != 1:
            letterCount[buffer] = 1


            return buffer

    return randint(0,nNodes-1)

#Appendes all current edges to a log file 
def logEdgesAppend(fp,graph,step):
    
        fp.write("Step: " + str(step) + "\t\t-EDGES-\n")
        
        for edge in graph.edges.data():
            fp.write('\t' + str(edge) +'\n')

#Function to remove nodes
def nodeFailure(g,n,step):
    
  global allFailedEdges
  global allFailedNodes  
  
  print("\t Removing node: " + n)
  buffer = g.edges(n)
  allFailedNodes.append(n)
  
  logFile = open('LogFile.txt',"a+")
  logFile.write("Step: "  + str(step) + "\t\t-NODE REMOVAL-\n")
  logFile.write("\tNode: " + n + " removed\n")
  logFile.close()

  for tuple in list(buffer):
    g.remove_edge(tuple[0],tuple[1])
    allFailedEdges.append(tuple)
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
  edgeTuple = (n1,n2)
  allFailedEdges.append(edgeTuple)
  return g

#Returns a tuple representing a random edge
def randomEdge(g):
    edgesList = list(g.edges())
    
    upperBound = len(edgesList)-1
    if upperBound <= 0:
        upperBound = 1
    buffer = edgesList[randint(0,upperBound)]  
    return buffer

def findPath(g,num):
    nodesList = list(g.nodes())
    
    
    
    
    
    numOfEdges = len(list(g.edges()))
    count = 0    
    while True & (count < numOfEdges):
        
        n1 = nodesList[randint(0,len(nodesList)-1)]
        n2 = nodesList[randint(0,len(nodesList)-1)]
        
        logFile = open('LogFile.txt',"a+")
        logFile.write("Step: " + str(num) + " ATTEMPT PACKET TRANSFER OVER: " + str(n1) + "  " + str(n2) +"\n" )
        logFile.close()
        
        print("Number of edges: " + str(numOfEdges) + " current count: " + str(count))
        try:
            print("Attempting to find a path between: " + n1 + ' and ' + n2)
        
            shortestPath = nx.dijkstra_path(g,n1,n2)
            logFile = open('LogFile.txt',"a+")
            logFile.write("\t" + str(list(shortestPath)) + "\n")
            logFile.close()
        
            return nx.dijkstra_path(g,n1,n2)
    
        except:
            count += 1
            logFile = open('LogFile.txt',"a+")
            logFile.write('\tNO PATH BETWEEN ' + str(n1) + ' TO ' + str(n2) + '\n') 
            logFile.close()
            
    return '\tNO PATH BETWEEN ' + str(n1) + ' TO ' + str(n2) + '\n'

def edgeListCreation(l):
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
    
    #Global references
    global Network
    global allFailedEdges
    global allFailedNodes
    
    #Randomly choosing if the network will have a failure
    if randint(0,3) == 1:
       #Randomly select if a node or a link will fail
        if randint(0,1) == 1:
            print(str(num) + ": Node has randomly failed ")
            Network = nodeFailure(Network,initialNodes[randint(0,len(initialNodes)-1)],num)
        else:
        
            if len(list(Network.edges.data())) > 1:
                print(str(num) + ": Link has randomly failed ")
        
                edgeBuffer = randomEdge(Network)
                Network = linkFailure(Network,edgeBuffer[0],edgeBuffer[1],num) 
    
    
    
    
    #Label the nodes
    nx.draw_networkx_labels(Network, NodePos, font_size=13)

    #Visualize the nodes 
    nx.draw_networkx_nodes(Network, NodePos, node_size=250, node_color='green')
    nx.draw_networkx_nodes(Network, NodePos, allFailedNodes, node_size=250, node_color='red', label = 'Failed node')

    #Visualize the edges
    labels = nx.get_edge_attributes(Network, 'weight')
    nx.draw_networkx_edges(Network, NodePos, width=.5, edge_color = 'black', label = 'Active links')
    
    #select 2 nandom nodes to send a packet between
    shortestPath = findPath(Network,num)
    if shortestPath[0] != '\t':
        shortestPathEdges = edgeListCreation(shortestPath)
        nx.draw_networkx_edges(Network, NodePos, shortestPathEdges, width=5, edge_color = 'green', label = 'Shortest path')
    
    nx.draw_networkx_edges(Network, NodePos, allFailedEdges, width=2, edge_color = 'red', label = 'Failed links', alpha=0.25)
    
    nx.draw_networkx_edge_labels(Network, NodePos, edge_labels=labels)
    
    ax.legend()

    #Logging current status of edges and nodes
    print(str(num) + ": loging edges")
    logEdgesAppend(logFile,Network,num)
    
    title = 'Network Simulation                                                Step: ' + str(num)
    
    plt.title(title, loc='left')
    
    
    plt.axis("off")
    
    logFile.close()

    return Network




#Random number for node generation
numberOfNodes = randint(15,26)

#Create graph
Network = nx.Graph()

#Node names
nodeNames = ['A','B','C','D','E','F','G','H','I'
            ,'J','K','L','M','N','O','P','Q','R'
            ,'S','T','U','V','W','X','Y','Z']

#Creating network nodes
initialNodes = []
for i in range(numberOfNodes):
  Network.add_node(nodeNames[i])
  initialNodes.append(nodeNames[i])
print("Network after nodes added")
print(Network)  

#Give each node a random position
NodePos = nx.spring_layout(Network)

#Random number for edge generation
numberOfEdge = randint(20,25)

#Label the nodes
nx.draw_networkx_labels(Network, NodePos, font_size=20)

#Declaring a tuple list of all failed edges
allFailedEdges = []
allFailedNodes = []

#Create initial network edges
#Making sure each node has an edge in the initial graph
letterCount = [0]*numberOfNodes
breakVal = 0
while breakVal != 1:
    parent = randint(0,numberOfNodes-1)
    Network.add_edge(initialNodes[parent] ,initialNodes[initialNodeCreation(parent,letterCount,numberOfNodes)] ,weight=randint(1,5))
    
    if 0 not in letterCount:
        breakVal = 1
#Adding 10 more edges
for i in range(50):
    parent = randint(0,numberOfNodes-1)
    Network.add_edge(initialNodes[parent] ,initialNodes[initialNodeCreation(parent,letterCount,numberOfNodes-1)] ,weight=randint(1,5))

#Visualize the nodes 
nx.draw_networkx_nodes(Network, NodePos, node_size=700, node_color='green')

#Visualize the edges
nx.draw_networkx_edges(Network, NodePos, width=2)

#Build the intial plt
fig, ax = plt.subplots(figsize=(10, 10))






'''
************Testing***************
'''

animationLength = 9000

'''
animation = matplotlib.animation.FuncAnimation(fig,
                                               networkUpdate, 
                                               frames = 30,
                                               interval = 10000, 
                                               repeat = True)
'''



#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Christian Stoldal'), bitrate=1800)
animation = animation.FuncAnimation(fig, networkUpdate, frames=35, interval=5000, repeat = False)
#animation.save('NetworkSim.mp4', writer=writer)

plt.show()

print('SIMULATION OVER')

#plt.show()
#.savefig('Test1.gif')

