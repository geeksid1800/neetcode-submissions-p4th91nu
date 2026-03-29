class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        The logic is we know how many elements are on either side of the median (n1+n2)/2, call it half.
        Let's say we choose first 'x' elements from nums1 (the smaller array), where x <= half, then we
        have to choose 'half-x' from nums2, and combining these two, we check whether that is truly
        the left half of the merged array. How do we do that? Well, every element in left half of merged
        <= every element in right half of merged array. Naturally the x elements in nums1 will be smaller
        than all the n1-x elements of nums1 chosen to be in the right half,and similarly for the 'half-x'
        chosen from nums2 to be in the left half of merged. However, if the largest element of the x
        is bigger than the smallest elements of right half chosen from nums2, we have selected too many
        elements from nums1 and we need to reduce x. Conversely, if largest element of 'half-x' is larger
        than the smallest elements of merged right half that were chosen from nums1, we have made x too
        small and need to increase it. Drawing an example:
        nums1 = [2,3,4,13] nums2 = [1,3,7,9,11,12] -> half = 5
        Let's say x=2, then we have cut the arrays as follows:
        nums1 =   [2,3] | [4,13]     => The two left halfs would combine to form left half of merged arr
        nums2 = [1,3,7] | [9,11,12]  => The two right halfs combine to form right half of merged arr
        The problem is that the merged array would have an element left of the median point that is
        bigger than an element right of the median (7>4). That tells us we should have chosen higher x so
        that 4 from nums1 gets included in the left half of merged array -> increase x
        So we employ binary search to finalise the value of x so that the largest element in each arr's
        left half <= the smallest element in each arr's right half.
        '''
        
        nums1,nums2 = (nums2,nums1) if len(nums2)<len(nums1) else (nums1,nums2) 
        #nums1 is always the shorter one now
        n1,n2 = len(nums1), len(nums2)

        half = (n1+n2+1)//2 #no of elements on left half of the merged array
        #we add 1 so that for odd n1+n2, we get the extra element as part of the left half

        l,r = 0, n1
        while l<=r:
            cut1 = (l+r)//2 #nums1 is partitioned [0,...cut1-1]|[cut1....n1-1]
            cut2 = half-cut1 #nums2 is partitioned [0...cut2-1]|[cut2...n2-1]

            l1 = nums1[cut1-1] if 0 <= cut1-1 else float('-inf')
            l2 = nums2[cut2-1] if 0 <= cut2-1 else float('-inf')

            r1 = nums1[cut1] if cut1 < n1 else float('inf')
            r2 = nums2[cut2] if cut2 < n2 else float('inf')
            '''if by chance we put all elements of either nums1 or nums2 on a single side of the merged
            array, we still need to be able to compare l2 vs r1 and l1 vs r2, so we initialise them so'''

            if (l1<=r2) and (l2<=r1):
                # we have segmented nums1 and nums2 correctly, just find the median now
                if (n1+n2)%2:
                    #since we have taken odd element as part of left half, the last element
                    #of left half of the merged array is simply the median
                    return max(l1,l2)
                
                else:
                    #for even sized merged array, one element of the median will be on last element on
                    #left side and the other will be on first element on right side, and we have to
                    #average them to get median
                    return (max(l1,l2) + min(r1,r2))/2.0
            
            elif (l1>r2):
                #l1 is clearly too big and needs to be on the right half in final array,
                #so make cut1 smaller
                r = cut1-1
            
            else:
                # l2 > r1, so r1 is too small and we need to make cut1 bigger so r1 comes in left half
                l = cut1 + 1