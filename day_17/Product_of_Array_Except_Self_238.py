class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Step 1: Calculate prefix products (left to right)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate suffix products (right to left) and multiply
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
"""

**Time:** O(n) - Optimal!  
**Space:** O(1) - Only using result array (output doesn't count)

---

## 📊 Visual Example:

**Input:** `nums = [1, 2, 3, 4]`

### **Step 1: Prefix Products (Left to Right)**
```
Index:     0    1    2    3
nums:      1    2    3    4
prefix:    1    1    2    6    (product of all elements BEFORE i)
result:   [1,   1,   2,   6]
```

| i | prefix (before i) | result[i] | New prefix |
|---|-------------------|-----------|------------|
| 0 | 1 | 1 | 1×1 = 1 |
| 1 | 1 | 1 | 1×2 = 2 |
| 2 | 2 | 2 | 2×3 = 6 |
| 3 | 6 | 6 | 6×4 = 24 |

### **Step 2: Suffix Products (Right to Left)**
```
Index:     0    1    2    3
nums:      1    2    3    4
suffix:   24   12    4    1    (product of all elements AFTER i)
result:   [1,   1,   2,   6]
         ×24  ×12   ×4   ×1
        ─────────────────────
result:  [24,  12,   8,   6]
"""