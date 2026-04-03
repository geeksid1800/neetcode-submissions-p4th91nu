'''
For a quicker O(nlogn) solution, we will maintain an ongoing 'arr'.
e.g. nums = [0,4,6,3,5,6]
1) Traverse through nums. If the current index 'i' is bigger than the last ele
in arr, then we straightforward add nums[i] to arr and move on. We get to i=2
like this, and arr=[0,4,6]
2) If i is smaller than arr[-1], (here i=3, 3<6), it can actually replace 4 (at
arr[1]) as [0,3] is a better subsequence than [0,4] (the last element is smaller
and both are same length). In fact, we need to find the first element >= nums[i]
in arr, and replace it. So arr is now [0,3,6]. We use BINARY SEARCH for this.
Note: This doesn't mean [0,3,6] is a valid subsequence. It means, so far, the
best subseq of length 2 we have ends with '3', and the best subseq of length 3
we have ends with '6'.
3) Next at i=4, again nums[i] < arr[-1] (5<6), so we find the first element in
arr larger than 5 and replace it. arr = [0,3,5]
4) At i=5, we can directly append 6, so now arr = [0,3,5,6] and ans = 4.
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [nums[0]] #min subseq length is 1.
        def bin_search(l,r,ele):
            #find the first element in arr[l,r] bigger than ele
            while l<r:
                m = (l+r)//2
                if arr[m] >= ele:
                    #possible answer, but could be a smaller one as well
                    r = m
                else: l = m+1
            return l
        
        for i in range(1,n):
            if nums[i] > arr[-1]:
                arr.append(nums[i])
            else:
                repl_ix = bin_search(0,len(arr)-1, nums[i])
                arr[repl_ix] = nums[i]
            print(f"{i=}, {arr=}")
        
        return len(arr)