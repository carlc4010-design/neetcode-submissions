class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i],0) + 1
        res = sorted(map,key = map.get,reverse = True)
        return res[0:k]
        
    
