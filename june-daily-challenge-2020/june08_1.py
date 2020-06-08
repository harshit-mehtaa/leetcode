class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(n):
            if 2**i > n:
                return False
            if 2**i == n:
                return True
        return False
