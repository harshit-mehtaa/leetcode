class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        res = ""
        for i in s:
            if i in t:
                res += i
                t = t[t.index(i)+1:]
               
        if res == s:
            return True
        else:
            return False
