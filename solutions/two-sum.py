class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            tmp = target - num
            tmp_list = nums[i+1:]
            if tmp in tmp_list:
                nums[i] = "mask"
                return [i, nums.index(tmp)]
                
        