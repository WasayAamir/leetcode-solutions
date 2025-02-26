class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        arr = []

        seen = set(nums1)

        for n in nums2:
            if n in seen:
                arr.append(n)
                seen.remove(n)
        return arr