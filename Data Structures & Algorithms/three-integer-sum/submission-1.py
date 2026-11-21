class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        nums = sorted(nums)
        for  k in range(len(nums)-1, -1, -1):
            if k < len(nums) - 1 and nums[k] == nums[k + 1]:
                continue
            a = 0 
            b = k - 1
            while b > a:
                if nums[a] + nums[b] + nums[k] == 0 :
                    res.append((nums[a],nums[b],nums[k]) )
                    b-=1
                    a+=1
                elif nums[a] + nums[b] + nums[k] > 0:
                    b -= 1
                elif nums[a] + nums[b] + nums[k] < 0:
                    a += 1    
        return [list(t) for t in set(res)]
                        