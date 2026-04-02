class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)
        
        while l <= r:
            partition1 = (l + r) // 2
            partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1

            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0  else float('-inf')
            maxLeft = max(maxLeft1, maxLeft2)

            minRight1 = nums1[partition1] if partition1 < len(nums1) else float('inf')
            minRight2 = nums2[partition2] if partition2 < len(nums2) else float('inf')
            minRight = min(minRight1, minRight2)

            if maxLeft <= minRight:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return maxLeft
                else:
                    return (maxLeft + minRight) / 2
            
            elif maxLeft1 > minRight2:
                r = partition1 - 1
            else:
                l = partition1 + 1
