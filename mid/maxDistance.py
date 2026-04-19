class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
    
        i = 0
        j = 0
        max_dist = 0

        for j in range (len(nums2)):
            while i < len(nums1) and i <= j and nums1[i] > nums2[j]:
                i += 1
            if i < len(nums1) and i <= j:
                max_dist = max(max_dist, j - i) 

        return max_dist


sol = Solution()
nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
print(sol.maxDistance(nums1, nums2))

