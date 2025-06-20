"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen, repeated = set(), set()
        for num in nums:
            if num in seen:
                repeated.add(num)
            seen.add(num)
        return (seen - repeated).pop()