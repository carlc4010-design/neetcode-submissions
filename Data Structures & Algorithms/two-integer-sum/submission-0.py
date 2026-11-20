class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
        for i in range(n):
            another = target - nums[i]
            if another in map:
                return [map[another],i]
            else:
                map[nums[i]] = i
        return []