def isBadVersion(version: int) -> bool:
    # This is a placeholder for the actual API call.
    # In practice, this function would be provided.
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # ✅ Versions start from 1
        first_bad = n
        
        while left <= right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                # This could be the answer, but check left for earlier
                first_bad = mid
                right = mid - 1  # Search left half
            else:
                # mid is good, first bad must be on the right
                left = mid + 1
        
        return first_bad
    
# Example usage:
sol = Solution()
# Assuming isBadVersion is defined elsewhere
print(sol.firstBadVersion(5))  # Output depends on isBadVersion implementation
print(sol.firstBadVersion(1))  # Output depends on isBadVersion implementation

"""
## 📝 Example Walkthrough

**Input:** `n = 5, bad = 4`
```
Versions: [good, good, good, bad, bad]
           1     2     3     4    5
```

### **Execution Trace:**

| Iteration | left | right | mid | isBadVersion(mid) | Action | first_bad |
|-----------|------|-------|-----|-------------------|--------|-----------|
| Init | 1 | 5 | - | - | - | 5 |
| 1 | 1 | 5 | 3 | False (good) | left = 4 | 5 |
| 2 | 4 | 5 | 4 | True (bad) | first_bad = 4, right = 3 | **4** |
| 3 | 4 | 3 | - | left > right | Exit | **4** |

**Visual:**
```
Step 1: Check version 3
[good, good, good, bad, bad]
              ↑
           mid=3 is good
           First bad must be right →

Step 2: Check version 4
[good, good, good, bad, bad]
                     ↑
                  mid=4 is bad!
                  Save as answer, check left for earlier →

Step 3: left > right, stop
Return first_bad = 4 ✅
```

**API calls:** Only 2 (vs your solution: 4 calls)

---

## 🎯 Why Binary Search?

### **Your Approach:**
```
n = 1,000,000,000
API calls: Up to 1,000,000,000
Time: TIMEOUT ❌
```

### **Binary Search:**
```
n = 1,000,000,000
API calls: ~30 (log₂(1,000,000,000) ≈ 30)
Time: Fast ✅
"""