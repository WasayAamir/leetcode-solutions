class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = defaultdict(int)

        for c in s:
            count[c] += 1  # Count occurrences in s

        for c in t:
            if count[c] == 0:  # If extra letter found
                return c
            count[c] -= 1  # Reduce count when matched


