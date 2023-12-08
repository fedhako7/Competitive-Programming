class Solution(object):
    def escapeGhosts(self, ghosts, target):
        # I can't scape if ghost is nearer to target than me.
        #My distance from target                                        
        distance = abs(target[0]) + abs(target[1])                      
        for pt in  ghosts:
            #Current ghost distance from target
            g_distance = abs(pt[0] - target[0]) + abs(pt[1] - target[1])
            if g_distance <= distance:
                return False
            
        return True
