# create-target-array-in-the-given-order
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for x in range(0, len(nums)):
            target.insert(index[x], nums[x])
            
        return target
