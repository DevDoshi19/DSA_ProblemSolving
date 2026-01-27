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
