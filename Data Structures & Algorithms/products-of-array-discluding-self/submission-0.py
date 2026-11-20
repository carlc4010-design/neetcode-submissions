class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res =  [0] * n
        pre =  [1] * n 
        pre[0] = nums[0] 
        post = [1]*n
        post[-1] = nums[-1] 
        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i] 
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i]
        for i in range(len(nums)):
            if i == 0:
                res[i] = post[1]
            elif i == len(nums)-1:
                res[i] = pre[n-2]
            else:
                res[i] = pre[i-1] * post[i+1] 
        return res