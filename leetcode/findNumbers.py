# find-numbers-with-even-number-of-digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # numbers with even number of digits
        nwenod = 0
        
        for num in nums:
            if num < 10**2 and num >= 10**1:
                nwenod += 1
            elif num < 10**4 and num >= 10**3:
                nwenod += 1
            elif num == 10**5:
                nwenod += 1
                    
        return nwenod
