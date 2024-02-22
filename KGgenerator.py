import random as rand
import string

nodeInputType = input("Node Input Type (R for random, M for manual): ")

nodes = []
nodesDict = {}

# MANUAL NODE CREATION
if (nodeInputType == 'M'):
    objNames = input("Enter node object names (separated with semicolons, don't use spaces):\n")
    objNamesList = objNames.split(';')
    
    # ALL OBJECTS ARE ATTRIBUTED OBJ LABEL BY DEFAULT
    for obj in objNamesList:
        nodesDict.update({obj:"OBJ"})
    
    objLabel = input("Label objects using Name:Label format (separated with semicolons). *USE ALL CAPS:\n")
    objLabelList = objLabel.split(';')

    # REPLACE MANUALLY LABELED OBJECTS
    for obj in objLabelList:
        pair = obj.split(':')
        if pair[0] in nodesDict.keys():
            nodesDict.update({pair[0]:pair[1]})
            
# RANDOMIZED NODE GENERATION   
elif (nodeInputType == 'R'):
    nodesCount = input("# of Nodes: ")
    
    for _ in range(int(nodesCount)):
        # RANDOM OBJECT NAME
        nodeName = rand.choice(string.ascii_uppercase) + rand.choice(string.ascii_uppercase) + rand.choice(string.ascii_uppercase)
        
        nodesDict.update({nodeName:"OBJ"})

# CREATING NODES
for node in nodesDict.keys():
    currentNode = "CREATE (" + node + ':' + nodesDict[node] + "{name:\"" + node + "\"})"
    nodes.append(currentNode) 
# print(nodes)


print('\n')
edgeInputType = input("Edge Input Type (R for random, M for manual): ")

edges = []
edgesDict = {}

# MANUAL EDGE CREATION
if (edgeInputType == "M"):
    nodePairs = input("Enter nodes to connect with an edge in Name-Name format (seperate with semicolon):\n")
    nodePairsList = nodePairs.split(';')
    
    # ADD EDGE TO EACH SPECIFIED NODE TO NODE CONNECTION
    for pair in nodePairsList:
        connectedNodes = pair.split('-')
        edgeName = input("Enter name of connection between\n" + connectedNodes[0] + " -> " + connectedNodes[1] + "\n")
        
        edgesDict.update({pair: edgeName})

# RANDOMIZED EDGE GENERATION
elif (edgeInputType == "R"):
    edgeProbability = float(input("Enter the probability for two nodes to have an edge as a decimal (e.g. 0.3): "))
    
    # FOR EACH PAIR OF NODES, APPLY RANDOM EDGE WITH GIVEN PROBABILITY
    for fromNode in nodesDict.keys():
        for toNode in nodesDict.keys():
            if (fromNode != toNode):
                if (rand.random() <= edgeProbability):
                    
                    edgeName = rand.choice(string.ascii_lowercase) + rand.choice(string.ascii_lowercase) + rand.choice(string.ascii_lowercase)
                    pairName = fromNode + ':' + toNode
                    
                    edgesDict.update({pairName:edgeName})

# CREATING EDGES
for edge in edgesDict.keys():
    nodePair = edge.split('-')
    fromNode = nodePair[0]
    toNode = nodePair[1]
    
    currentEdge = "CREATE (" + fromNode + ")-[:" + edgesDict[edge] + "]->(" + toNode + ")"
    edges.append(currentEdge)
# print(edges)


# PRINT CYPHER QUERY
for node in nodes:
    print(node)
print('\n')
for edge in edges:
    print(edge)
