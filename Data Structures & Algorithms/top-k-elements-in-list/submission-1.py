class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        h = []
        for num in count.keys():
            heapq.heappush(h, (count[num], num))
            if len(h) > k:
                heapq.heappop(h)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(h)[1])
        return res