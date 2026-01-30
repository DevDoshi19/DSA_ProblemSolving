# ⛰️ Binary Search Climb | O(log n) | One Direction Check | Beats 99%

## 💡 Intuition
Finding a peak is like climbing a mountain - **always walk uphill and you'll reach a peak!**

**Key Insight:** We don't need to check both neighbors. Just compare `mid` with `mid+1`:
- If going **uphill** (`nums[mid] < nums[mid+1]`) → Peak is ahead, search right
- If going **downhill** (`nums[mid] > nums[mid+1]`) → Peak is here or behind, search left

Since array extends to `-∞` on both ends, we're **guaranteed to find a peak**!

---

## 🚀 Approach

**Greedy climb strategy:**

1. Compare `nums[mid]` with `nums[mid+1]`

2. **If `nums[mid] > nums[mid+1]`:** (Descending)
   - Peak is at `mid` or to the left
   - Search left: `right = mid`

3. **If `nums[mid] < nums[mid+1]`:** (Ascending)
   - Peak must be to the right
   - Search right: `left = mid + 1`

4. When `left == right`, we found a peak!

---

## 💻 Code

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # Descending: peak is at mid or left
                right = mid
            else:
                # Ascending: peak is on right
                left = mid + 1
        
        return left  # left == right
```

---

## 📝 Example Walkthrough

**Input:** `nums = [1,2,3,1]`

```
Step 1: left=0, right=3, mid=1
[1, 2, 3, 1]
    ↑  ↑
  2 < 3 → going uphill → search right
  left = 2

Step 2: left=2, right=3, mid=2
[1, 2, 3, 1]
       ↑  ↑
  3 > 1 → going downhill → peak here or left
  right = 2

Step 3: left=2, right=2 → STOP
Return 2
```

**Output:** `2` (nums[2] = 3 is a peak) ✅

---

## 🎨 Visual Logic

```
Case 1: Ascending
[1, 2, 3, 1]
    ↑  ↑
   Going UP
   
→ Peak must be ahead →

Case 2: Descending  
[1, 2, 3, 1]
       ↑  ↑
   Going DOWN
   
← Peak is here or behind ←
```

---

## 📊 Complexity

- **Time:** O(log n) - Binary search halves space each time
- **Space:** O(1) - Only using pointers

---

## 💡 Why It Works

**Key properties:**
1. Array extends to `-∞` on both ends (given)
2. No two adjacent elements are equal (given)
3. **Always move toward higher ground** → guaranteed to reach a peak
4. If multiple peaks exist, we return ANY one (problem allows this)

**Why we don't check both neighbors:**
- One direction is enough to decide where the peak is!
- Checking `mid+1` tells us if we're climbing or descending

---

## 🔍 Edge Cases

```python
# Single element
nums = [1] → Output: 0

# All ascending
nums = [1,2,3,4,5] → Output: 4 (last)

# All descending  
nums = [5,4,3,2,1] → Output: 0 (first)

# Multiple peaks (any valid)
nums = [1,2,1,3,5,6,4] → Output: 1 or 5
```

---

## 🎓 Key Takeaway

**Think of it as climbing:** Always step toward higher ground, and you'll reach the top!

No need to overthink - just compare with one neighbor and follow the slope upward.

---

## 🏷️ Tags
`#BinarySearch` `#Array` `#GreedyClimb` `#Medium` `#Clever`
