# LeetCode 560: Subarray Sum Equals K

## Problem Statement

Given an array of integers `nums` and an integer `k`, find the total number of continuous subarrays whose sum equals `k`.

**Example:**

*   **Input:** `nums = [1, 1, 1]`, `k = 2`
*   **Output:** `2`
    *   The subarrays are `[1, 1]` (starting at index 0) and `[1, 1]` (starting at index 1).

*   **Input:** `nums = [1, 2, 3]`, `k = 3`
*   **Output:** `2`
    *   The subarrays are `[1, 2]` and `[3]`.

## Thinking Through the Problem

### The Brute-Force Approach (and why it's not ideal)

The most straightforward way to solve this is to generate every possible subarray, calculate its sum, and check if it equals `k`.

```python
# Conceptual brute-force logic
count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        current_sum = sum(nums[i:j+1])
        if current_sum == k:
            count += 1
return count
```

This involves two nested loops, making the time complexity **O(n²)**. With an input array size up to 20,000, this would be too slow and likely result in a "Time Limit Exceeded" error on platforms like LeetCode.

### The Better Approach: Prefix Sums

A more efficient method is to use the concept of **prefix sums**. A prefix sum at an index `i` is the sum of all elements from the start of the array up to `i`.

Let's say we have a running sum `prefix_sum` as we iterate through the array. We are looking for a subarray ending at the current position `j` that sums to `k`.

Let the `prefix_sum` at index `j` be `sum_j`.
Let the `prefix_sum` at a previous index `i` be `sum_i`.

The sum of the subarray between `i+1` and `j` is `sum_j - sum_i`. We want this to be equal to `k`.

`sum_j - sum_i = k`

If we rearrange this equation, we get:

`sum_i = sum_j - k`

This is the key insight! As we iterate through the array and calculate our current `prefix_sum` (let's call it `current_sum`), we need to know how many times we have previously seen a prefix sum of `current_sum - k`. If we have, then each occurrence represents a new subarray that sums to `k`.

### Using a Hash Map for Efficiency

To quickly look up how many times a specific prefix sum has occurred, a **hash map** (or a dictionary in Python) is the perfect tool. The map will store the prefix sums as keys and their frequencies (how many times they've appeared) as values.

## The Implemented Solution: Step-by-Step

The provided solution uses this optimized hash map and prefix sum approach.

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_map = {0: 1} # Key: prefix_sum, Value: frequency
        
        for num in nums:
            # 1. Update the running prefix sum
            prefix_sum += num
            
            # 2. Check for the complement
            # We are looking for a previous prefix_sum that equals `prefix_sum - k`
            if prefix_sum - k in prefix_map:
                # If it exists, we add its frequency to our count
                count += prefix_map[prefix_sum - k]
            
            # 3. Update the map with the current prefix sum
            # Add the current prefix_sum to the map, or increment its count if it's already there
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        
        return count
```

**Why initialize `prefix_map = {0: 1}`?**

This is a crucial edge case. It handles subarrays that start from the beginning of the array (index 0). If the `prefix_sum` itself equals `k`, then `prefix_sum - k` will be `0`. We need the lookup for `0` to succeed, indicating that we found a subarray of sum `k` that starts from the very first element. The `1` signifies that a sum of `0` (the "empty" prefix before the array starts) has been seen once.

## How to Identify and Apply This Pattern

**When to think about Prefix Sums + Hash Map:**

You should consider this pattern for problems that involve finding **subarrays** or **subsequences** with a specific **sum** property.

**Key Indicators:**

1.  **"Subarray" or "Subsequence":** The problem asks you to analyze a contiguous or non-contiguous part of a sequence.
2.  **"Sum":** The core condition is related to the sum of elements (e.g., equals `k`, is divisible by `k`, is a multiple of `k`).
3.  **Efficiency is Required:** A brute-force O(n²) approach seems too slow based on the input constraints.

**Where to Apply This Approach:**

This technique is a cornerstone for many array-based problems. It's not just for finding sums equal to `k`. It can be adapted for variations like:

*   **Longest Subarray with Sum `k`:** Instead of a count, you would store the *index* of the prefix sum in the hash map and calculate the length.
*   **Subarray Sum Divisible by `k`:** Instead of `prefix_sum - k`, you would work with `prefix_sum % k`. The logic is similar: if `(prefix_sum_j % k) == (prefix_sum_i % k)`, then the subarray between `i` and `j` has a sum divisible by `k`.
*   **Problems involving ranges:** Any problem where you need to calculate the sum of a range repeatedly is a candidate for prefix sums. The hash map is the optimization that prevents you from re-calculating or iterating multiple times.

By mastering this pattern, you'll be able to solve a wide range of medium-to-hard level array problems efficiently.
