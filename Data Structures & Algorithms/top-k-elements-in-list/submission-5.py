class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        myMap = {}
        frequnt = [[] for _ in range(n + 1)] 
        #maxV = 0 
        for i in range(n):
            myMap[nums[i]] = myMap.get(nums[i],0) + 1
        for c in myMap:
            frequnt[myMap[c]].append(c)
            #maxV = max(myMap[c],maxV)
        res = []
        for i in range(n,0,-1):
            for c in frequnt[i]:
                res.append(c)
                if len(res) == k:
                    return res
        return res
            