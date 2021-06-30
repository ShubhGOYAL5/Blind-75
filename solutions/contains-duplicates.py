class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True
        # isPresent = (len(set(nums)) == len(nums))
        # return !isPresent
        