# 📅 Day 4 — Sliding Window (Variable Size)

On Day 4 of my **DSA / Problem Solving journey**, I focused on mastering the
**Variable Size Sliding Window** pattern.

Unlike fixed-size windows, here the window **expands and shrinks dynamically**
based on a condition. These two problems helped me clearly understand *when to
expand* and *when to shrink* the window.

---

## 🔹 Problem 1: Longest Substring Without Repeating Characters

**Problem Statement**  
Given a string `s`, find the length of the longest substring without repeating characters.

**Pattern Used:** Variable Size Sliding Window  
**Key Concept:** Maintain a window of unique characters using a set.

### 🧠 Approach
- Use two pointers: `left` and `right`
- The `right` pointer expands the window
- A set `seen` stores unique characters in the current window
- If a duplicate character is found:
  - Shrink the window from the left
  - Remove characters from the set until the window becomes valid again
- Track the maximum window size during the process

### ✅ Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_count = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_count = max(max_count, right - left + 1)

        return max_count
````

### ⏱ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(k)`
  (where `k` is the number of unique characters in the window)

---

## 🔹 Problem 2: Minimum Size Subarray Sum

**Problem Statement**
Given an array of positive integers `nums` and an integer `target`,
return the minimal length of a contiguous subarray whose sum is **greater than or equal to `target`**.
If no such subarray exists, return `0`.

**Pattern Used:** Variable Size Sliding Window
**Key Concept:** Expand to reach condition, shrink to minimize window size.

### 🧠 Approach

* Use two pointers: `left` and `right`
* Maintain a running sum of the current window
* Expand the window by moving `right` and adding elements to the sum
* When the sum becomes `>= target`:

  * Update the minimum window length
  * Shrink the window from the left to find a smaller valid window
* Continue until all elements are processed

### ✅ Code

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
```

### ⏱ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## ✅ Key Learnings from Day 4

* Variable size sliding window problems require **controlled shrinking**
* Each element enters and leaves the window at most once
* A `while` loop inside a `for` loop does **not** mean `O(n²)`
* Understanding *when to shrink* is more important than writing code fast

---

📌 **Next Focus:** More Sliding Window problems and real interview patterns 🚀
📈 Building consistency one day at a time.

```

---

### 💡 Small GitHub Tip
Inside your repo, you can structure it like this:

```

day_04_sliding_window/
├── longest_substring.py
├── min_size_subarray.py
└── README.md

