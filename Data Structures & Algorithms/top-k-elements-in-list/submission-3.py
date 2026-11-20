class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        myMap = {}
        frequnt = [[] for _ in range(n + 1)] 
        maxV = 0 
        for i in range(n):
            myMap[nums[i]] = myMap.get(nums[i],0) + 1
        for c in myMap:
            frequnt[myMap[c]].append(c)
            maxV = max(myMap[c],maxV)
        res = []
        i = k
        while i > 0:
            if  frequnt[maxV]:
                res.append(frequnt[maxV].pop())
                i -=  1
            elif maxV > 0:
                maxV -= 1
        return res
            