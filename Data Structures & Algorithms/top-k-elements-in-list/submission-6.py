class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        n = len(nums)
        busket = [[] for _ in range(n + 1)] 
        res = [] 
        for i in range(n):
            myMap[nums[i]] = myMap.get(nums[i],0) + 1
        for c in myMap:
            busket[myMap[c]].append(c)
        for i in range(n,0,-1):
           for j in busket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res