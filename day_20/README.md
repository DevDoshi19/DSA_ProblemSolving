# 🎯 Binary Search Pattern | O(log n) | Lower Bound | Beats 100%

## 💡 Intuition
Finding the first bad version is like finding a spoiled apple in a sorted row - once you find one bad apple, all apples after it are also bad. We don't need to check every apple, just use binary search!

**Key Idea:** Find the **first** position where `isBadVersion()` returns `true`.

---

## 🚀 Approach

Same as **Search Insert Position** - it's the lower bound pattern!

1. **If `isBadVersion(mid) == true`:**
   - This could be the answer
   - But check left for an earlier bad version
   - Save answer and search left: `first_bad = mid, right = mid - 1`

2. **If `isBadVersion(mid) == false`:**
   - This version is good
   - First bad must be on the right
   - Search right: `left = mid + 1`

---

## 💻 Code

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        first_bad = n
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1  # Check left for earlier bad
            else:
                left = mid + 1   # Search right
        
        return first_bad
```

---

## 📝 Example

**Input:** `n = 5, bad = 4`

```
Versions: [good, good, good, bad, bad]
           1     2     3     4    5

Step 1: mid=3 → good → search right
Step 2: mid=4 → bad  → save and search left
Step 3: left > right → return 4
```

**API Calls:** Only 2 (vs linear search: 4)

---

## 📊 Complexity

- **Time:** O(log n) - Binary search
- **Space:** O(1)
- **API Calls:** O(log n) - Critical for this problem!

---

## 💡 Why Binary Search?

```
n = 1,000,000,000

Linear search: 1 billion API calls → TIMEOUT ❌
Binary search: ~30 API calls → Fast! ✅
```

---

## 🔑 Key Pattern

This is **Lower Bound** - same pattern as Problem 35 (Search Insert Position)!

```python
# Generic lower bound template:
if condition_is_true(mid):
    answer = mid
    right = mid - 1  # But keep searching left
else:
    left = mid + 1
```

---

## 🏷️ Tags
`#BinarySearch` `#LowerBound` `#Interactive` `#Easy`

---

**💖 Upvote if helpful! 👍**

# 🎯 Classic Binary Search | O(log n) | Clean Template | Beats 99%

## 💡 Intuition
Binary search is like finding a word in a dictionary - you don't start from page 1, you open the middle and decide which half to search next!

**Key Idea:** Eliminate half the search space in each step.

---

## 🚀 Approach

**Simple 3-step logic:**

1. **Check middle element:**
   - If `nums[mid] == target` → Found it! ✅
   
2. **Decide direction:**
   - If `nums[mid] > target` → Target is smaller → Search **LEFT** half
   - If `nums[mid] < target` → Target is larger → Search **RIGHT** half

3. **Repeat** until found or search space exhausted

---

## 💻 Code

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1  # Search left
            else:
                left = mid + 1   # Search right
        
        return -1  # Not found
```

---

## 📝 Example Walkthrough

**Input:** `nums = [-1,0,3,5,9,12], target = 9`

```
Step 1: left=0, right=5, mid=2
        nums[2]=3 < 9 → go right

Step 2: left=3, right=5, mid=4
        nums[4]=9 == 9 → Found! Return 4
```

**Output:** `4`

---

## 📊 Complexity

- **Time:** O(log n) - Halves search space each iteration
- **Space:** O(1) - Only using pointers

---

## 💡 Key Points

**Why `left <= right` not `left < right`?**
```python
nums = [5], target = 5
With <  : Skips when left==right → Wrong! ❌
With <= : Checks when left==right → Correct! ✅
```

**Memory Trick:**
- `mid > target` → go LEFT (smaller values)
- `mid < target` → go RIGHT (larger values)

---

## 🏷️ Tags
`#BinarySearch` `#Array` `#Easy` `#Template` `#Fundamentals`

---

**💖 Upvote if this helped! 👍**
```
