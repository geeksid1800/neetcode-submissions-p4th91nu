class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Fill backwards, largest-first, since we have n 0s at the end
        last = len(nums1)-1
        p1, p2 = m-1, n-1

        while (p1>=0 and p2>=0):
            if (nums1[p1] >= nums2[p2]):
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
        
        while(p2 >= 0):
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1
        
        while(p1 >= 0):
            nums1[last] = nums1[p1]
            p1 -= 1
            last -= 1