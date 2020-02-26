"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        max_so_far = nums[0]
        max_end_Sum = 0
        for i in range(0,len(nums)):
            max_end_Sum += nums[i]
            if max_so_far < max_end_Sum:
                max_so_far = max_end_Sum 
            if max_end_Sum < 0:
                max_end_Sum = 0
            
        return max_so_far
                
        
