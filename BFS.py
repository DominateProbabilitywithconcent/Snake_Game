class BFS:
    def __init__(self,start_pos,end_pos,depth):
        self.star_pos = start_pos
        self.end_pos = end_pos
        self.depth = depth
    def getNeighbors(self,position):
        neighbors = [[position[0] + 1, position[1]],
                     [position[0] - 1, position[1]],
                     [position[0], position[1] + 1],
                    [position[0], position[1] - 1]]
        return neighbors
    def BFSpathfinding(self,board):
        queue = []
        queue.insert(0,self.start_pos)
        visited = set([self.start_pos])
        goal = 0
        while queue != 0:
            path = queue.pop(0)
            x,y = path[-1]
            if (x,y) == self.end_pos:
                return path
            
                
            
            
            
        return goal
            
            
        
        
        
        