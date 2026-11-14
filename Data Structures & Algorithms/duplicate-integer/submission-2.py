class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        print(nums)
        previous_num = None
        for number in nums:
            if previous_num == number:
                return True
            else:
                previous_num = number
        return False 
        