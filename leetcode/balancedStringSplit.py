class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r, res = 0, 0, 0
        
        for i in range(0,len(s)):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            
            if l == r:
                res += 1
                
        return res