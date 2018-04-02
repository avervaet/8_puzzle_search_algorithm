# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 19:02:39 2018

@author: Arthur Vervaet
"""


initialState = [1,2,5,3,4,0,6,7,8]
goalState = [0,1,2,3,4,5,6,7,8]



def bfs(initialState,goalState):
    frontier = []
    frontier.append(initialState)
    explored = []
    
    while frontier != []:
        
        state = frontier[0]
        del frontier[0]
        explored.append(state)
        
        if state == goalState:
            print(state)
            return "Success"
        
        neighbors = getNeighbors(state)
        for neigbhor in neighbors :
            if not neigbhor in explored:
                if not neigbhor in frontier:
                    frontier.append(neigbhor)
                    
    return "Failure"

def getNeighbors(state):
    i = state.index(0)
    neighbors = []
    print(state)
    
    if i>2 :
        neighbor = list(state)
        neighbor[i], neighbor[i-3] = neighbor[i-3], neighbor[i]
        neighbors.append(neighbor)
        print('Up')
 
    print(state)
    
    if i<6:
        neighbor = list(state)
        neighbor[i], neighbor[i+3] = neighbor[i+3], neighbor[i]
        neighbors.append(neighbor)
        print('Down')
        
    if not i in [0,3,6]:
        neighbor = list(state)
        neighbor[i], neighbor[i-1] = neighbor[i-1], neighbor[i]
        neighbors.append(neighbor)
        print('Left')
        
    if not i in [2,5,8]:
        neighbor = list(state)
        neighbor[i], neighbor[i+1] = neighbor[i+1], neighbor[i]
        neighbors.append(neighbor)
        print('Right')
        
    return neighbors


        
bfs(initialState,goalState)