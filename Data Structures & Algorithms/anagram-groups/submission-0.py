class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        for i in range(len(strs)):
            count = [0]* 26
            for c in strs[i]:
                count[ord(c)-ord("a")] += 1
            key = tuple(count)
            if key not in group:
                group[key] = []
            group[key].append(strs[i])
        return list(group.values())


