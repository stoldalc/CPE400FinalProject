# CPE400FinalProject
Dynamic Routing Mechanism in Faulty Network nodes or Links

# Libraries used
```Python
NetworkX
MatPlotLib
Random
```
## Description
This is a simulation with a visual display of a mesh network that has the potential for link and node failures. In the event of a failure of a link, the network will have to find the shortest path creating links to reconnect any lost nodes. In the event of a node failure, the network will have to adapt and create links if the failed node is preventing or delaying network traffic. The network will need to be able to detect when a node or link has failed and removed it from the list of active working nodes and links. This will be simulated with each node or link having a randomly generated potential to fail as well as the ability for the user using the demo to select a node or link to fail on command. While I need to do more research on how I will be implementing this I will likely use Java or Python.
