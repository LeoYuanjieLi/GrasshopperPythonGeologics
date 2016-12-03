import rhinoscriptsyntax as rs
import math

Vertices = rs.MeshVertices(Mesh) # Get Mesh Vertices
#Get Mesh UV value 
uvValue = int(math.sqrt(len(Vertices)))


pList = []
#BlackList is storing the points that we don't want at the edge
BlackList = []
for k in range(uvValue):
    BlackList.append(k*uvValue)
    BlackList.append(k*uvValue - 1)
    
print BlackList


for i in range(0,len(Vertices)):
#for each point, check if it is the lowest of its neighbours
    if (i not in BlackList) and (i >= uvValue) and (i < len(Vertices) - uvValue) and (Vertices[i][2] < Vertices[i+1][2]) and (Vertices[i][2] < Vertices[i-1][2])and (Vertices[i][2] < Vertices[i+uvValue][2])and (Vertices[i][2] < Vertices[i-uvValue][2])and (Vertices[i][2] < Vertices[i-1-uvValue][2])and (Vertices[i][2] < Vertices[i+1-uvValue][2])and (Vertices[i][2] < Vertices[i-1+uvValue][2])and (Vertices[i][2] < Vertices[i+1+uvValue][2]):
        pList.append(Vertices[i])

a = pList
