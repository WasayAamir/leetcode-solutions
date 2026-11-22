class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}                     #label -> list of words
        for word in strs:
            baseline = "".join(sorted(word))
            if baseline not in groups:
                groups[baseline] = []
            groups[baseline].append(word)
        return list(groups.values())

