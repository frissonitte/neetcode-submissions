from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for s in strs:
            count = tuple(sorted(s))

            dict[count].append(s)

        return list(dict.values())