class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] +=1

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        output = []
        for i in range(k):
            output.append(sorted_items[i][0])
        return output