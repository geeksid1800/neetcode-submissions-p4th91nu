class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        #reversing the list will bring the last elements to the front.
        #then reversing the first k and rest (n-k) separately will restore
        #their relative internal order
        # [1,2,3,4,5] k = 2 -> [(5,4),(3,2,1)] -> [(4,5),(1,2,3)]
        def reverse_substring(arr,l,r):
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
        
        reverse_substring(nums,0,n-1)
        reverse_substring(nums,0,k-1)
        reverse_substring(nums,k,n-1)

            