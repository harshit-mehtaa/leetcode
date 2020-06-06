class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        n = len(costs)
        m = int(n/2)
        
        diff = sorted(costs, key= lambda x: x[0]-x[1])
        
        for i in range(0, m):
            total += diff[i][0]
        for i in range(m, n):
            total += diff[i][1]
            
        return total
