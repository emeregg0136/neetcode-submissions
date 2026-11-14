class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            if counts.get(num) == None:
                counts[num] = 1
            else:
                counts[num] += 1
        
        pairs = sorted(list(counts.items()), key=lambda x:x[1], reverse=True)[:k]

        top_k = []
        for pair in pairs:
            top_k.append(pair[0])

        return top_k
