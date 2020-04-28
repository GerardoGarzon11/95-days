class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum([1 for x in nums if x < num]) for num in nums]
