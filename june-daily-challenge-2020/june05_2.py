class Solution:

    def __init__(self, w: List[int]):
        wSum = sum(w)
        currSum = 0
        self.list = []
        for i in w:
            currSum += i / wSum
            self.list.append(currSum)
            
    def pickIndex(self) -> int:
        return bisect.bisect_left(self.list, random.random())
