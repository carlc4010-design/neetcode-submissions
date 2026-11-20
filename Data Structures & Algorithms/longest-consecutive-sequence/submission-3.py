class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0
        for c in nums:
            length = 1
            if c - 1  in mySet:
                continue
            n = c + 1
            while n in mySet:
                length += 1
                n += 1
            longest = max(longest,length)
        return longest
