from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        for i in ctr:
            if ctr[i] > 1:
                return True
        return False