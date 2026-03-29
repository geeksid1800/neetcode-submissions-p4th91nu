class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i,j = 0, 0
        n = len(nums)

        for j in range(n):
            if nums[j] in window:
                return True
            window.add(nums[j])

            if (j-i)==k: #reached max window size
                window.remove(nums[i])
                i += 1
                
        return False 
