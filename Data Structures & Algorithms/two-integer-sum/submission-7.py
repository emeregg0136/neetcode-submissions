class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            indices[num] = i 
            # if there are duplicate values, key = largest index
            # this achieves the minimum index requirement in the next loop

        for i,n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return []

                
