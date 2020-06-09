class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        
        s_index = 0
        
        for t_index in range(len(t)):
            if s_index == len(s):
                return True
            if s[s_index] == t[t_index]:
                s_index += 1
        if s_index == len(s):
            return True
        else:
            return False
