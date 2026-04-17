from typing import List
from math import inf

class Solution:
    """
    Find the minimum distance between indices of mirror number pairs.

    Args:
        nums: List of integers to search for mirror pairs

    Returns:
        Minimum distance between mirror pairs, or -1 if no mirrors exist
    """
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])
            prev[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [123, 321, 456, 654],      # Result: 1 (123-321 at indices 0-1)
        [1, 2, 3],                  # Result: -1 (no mirror pairs)
        [101, 101],                 # Result: 1 (101 is mirror of itself)
        [12, 21, 34, 43, 56, 65],   # Result: 1 (12-21 at indices 0-1)
        [9876, 6789, 555],          # Result: 1 (9876-6789 at indices 0-1)
    ]

    for i, nums in enumerate(test_cases):
        result = solution.minMirrorPairDistance(nums)
        print(f"Test case {i+1}: nums = {nums}")
        print(f"Result: {result}\n")
