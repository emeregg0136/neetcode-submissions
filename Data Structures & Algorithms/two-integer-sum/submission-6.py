class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums)-1

        while i < j:
            the_sum = A[i][0] + A[j][0]
            if the_sum == target:
                return sorted([A[i][1], A[j][1]])
            elif the_sum < target:
                i += 1
            elif the_sum > target:
                j -= 1



