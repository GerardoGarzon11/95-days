class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while num:
            # explanation
            """
                num & 1 = num AND 1
                therefore if true, that means it is and odd number
                so we'll subtract and then divide (that's two steps)
                if false, we'll divide (one step)
                only case where this doesn't apply is with 1
                because we only need to subtract
            """
            steps += 2 if num & 1 else 1
            num >>= 1
        return steps - 1