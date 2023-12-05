class Solution(object):
    def wateringPlants(self, plants, capacity):
        #Tracks the number of steps
        no_steps = 0
                                                                   
        leftWater = capacity                          
        for idx in range(len(plants)):
            no_steps += 1                                  
            leftWater -= plants[idx]                             
            if idx <= (len(plants) -2) and leftWater < plants[idx + 1]:
                no_steps += 2 * (idx + 1)
                leftWater = capacity

        return no_steps