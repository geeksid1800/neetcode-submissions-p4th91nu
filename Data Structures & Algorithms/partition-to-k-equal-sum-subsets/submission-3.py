'''
Calculate the sum of all numbers in the array. If it is not divisible by k, return False since equal subsets cannot be formed.
Sort the array in descending order. Sorting helps with pruning, allowing us to quickly skip certain numbers during the DFS search.
Create a boolean array, used, to keep track of which numbers have been used in the subsets. Initially, all elements are set to False.
Implement a recursive DFS function, dfs, which takes three parameters:
    sub_sets_count: The number of subsets found so far.
    cur_sum: The sum of the current subset being constructed.
    start_index: The index of the next number to consider in the array.

In the DFS function:
    If sub_sets_count equals k, we have found k subsets with equal sums, so we return True.
    If cur_sum equals target_sum, we move to the next subset by making a recursive call with sub_sets_count + 1, 0, and 0 as the updated parameters.
    Iterate through the remaining numbers in the array, starting from start_index:
        If the current number has already been used or adding it to cur_sum exceeds target_sum, skip it.
        Implement the pruning step: If the current number is equal to the previous number and the previous number has not been used, skip the current number. This helps avoid duplicate computation and improves efficiency.
        Mark the current number as used by setting used[i] to True.
        Recursively call dfs with the updated sub_sets_count, cur_sum, and i + 1.
        If the recursive call returns True, it means we have found a valid partition, so we can immediately return True.
        Undo the choice of using the current number by setting used[i] back to False.
If no solution is found from the DFS search, return False.
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Calculate the sum of all numbers in the array
        nums_sum = sum(nums)
        # If the sum cannot be evenly divided by k, it is not possible
        if nums_sum % k != 0:
            return False

        # Calculate the target sum for each subset
        target_sum = nums_sum // k
        # Sort the array in descending order to optimize pruning
        nums.sort(reverse=True)
        # Keep track of which numbers have been used in subsets
        used = [False] * len(nums)

        # Depth-first search function to explore all possible subsets
        def dfs(sub_sets_count, cur_sum, start_index):
            # If we have found k subsets, it is a valid partition
            if sub_sets_count == k:
                return True
            # If the current subset sum matches the target sum, move to the next subset
            if cur_sum == target_sum:
                return dfs(sub_sets_count + 1, 0, 0)
            
            # Iterate through the remaining numbers in the array
            for i in range(start_index, len(nums)):
                # If the number has been used or adding it exceeds the target sum, skip it
                if used[i] or cur_sum + nums[i] > target_sum:
                    continue
                
                # Pruning step: if the current number is the same as the previous number
                # and the previous number hasn't been used, skip the current number
                if i > start_index and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # Mark the current number as used
                used[i] = True
                # Recursive call to explore the next number and update the subset sum
                if dfs(sub_sets_count, cur_sum + nums[i], i + 1):
                    return True
                # Undo the choice of using the current number and try the next number in the array
                used[i] = False

            # If no solution is found, return False
            return False

        # Start the depth-first search from the beginning of the array with an empty subset
        return dfs(0, 0, 0)
