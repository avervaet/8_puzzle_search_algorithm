# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 19:02:39 2018

@author: Arthur Vervaet
"""
class node:
    
        def __init__(self,state,parent,move):
            self.state = state 
            self.parent = parent
            self.move = move
        
        def getNeighbors(self):
            i = self.state.index(0)
            neighbors = []
            
            if i>2 :
                neighbor = node(list(self.state),self,'Up')
                neighbor.state[i], neighbor.state[i-3] = neighbor.state[i-3], neighbor.state[i]
                neighbors.append(neighbor)
            
            if i<6:
                neighbor = node(list(self.state),self,'Down')
                neighbor.state[i], neighbor.state[i+3] = neighbor.state[i+3], neighbor.state[i]
                neighbors.append(neighbor)
                
            if not i in [0,3,6]:
                neighbor = node(list(self.state),self,'Left')
                neighbor.state[i], neighbor.state[i-1] = neighbor.state[i-1], neighbor.state[i]
                neighbors.append(neighbor)
                
            if not i in [2,5,8]:
                neighbor = node(list(self.state),self,'Right')
                neighbor.state[i], neighbor.state[i+1] = neighbor.state[i+1], neighbor.state[i]
                neighbors.append(neighbor)
                
            return neighbors
  
initialNode = node([1,2,5,3,4,0,6,7,8],None,'Init')
goalNode = node([0,1,2,3,4,5,6,7,8],None,'End')



def bfs(initialState,goalState):
    frontier = [initialState]
    explored = []
    
    while frontier != []:
        
        currentNode = frontier[0]
        del frontier[0]
        explored.append(currentNode)
        
        if currentNode.state == goalNode.state:
            showPath(currentNode)
            return "Success"
        
        neighbors = currentNode.getNeighbors()
        for neigbhor in neighbors :
            if not neigbhor in explored:
                if not neigbhor in frontier:
                    frontier.append(neigbhor)
                    
    return "Failure"      

def showPath(node):
    path = []
    while node != None:
        path.append(node.move)
        previous = node.parent
        node = previous
    path = path[::-1]
    print (path)

bfs(initialNode,goalNode)