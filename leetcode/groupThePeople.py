class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        for size in range(1, max(groupSizes) + 1):
            current_group = []
            for x in range(0, len(groupSizes)):
                if groupSizes[x] == size:
                    # person can get in group
                    if len(current_group) != groupSizes[x]:
                        current_group.append(x)
                    # person can't get in group
                    else:
                        groups.append(current_group)
                        current_group = [x]
            if len(current_group) != 0:
                groups.append(current_group)
        
        return groups