class Solution:
    def change(self, amount: int, coins: List[int]) -> int:      
        f = [0] * (amount + 1)
        f[0] = 1
        
        for coin in coins:
            for i in range(amount+1):
                if i - coin >= 0:
                    f[i] += f[i-coin]
        return f[amount]
