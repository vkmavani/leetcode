"""
Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = dict()

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in the dictionary
            if complement in num_indices:
                # If found, return the indices
                return [num_indices[complement], i]

            # Otherwise, store the current number and its index
            num_indices[num] = i