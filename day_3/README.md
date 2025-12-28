# 🚀 Day 3 – DSA / Problem Solving Journey

**Problem:** LeetCode 1456 — *Maximum Number of Vowels in a Substring of Given Length*  
**Technique Used:** Sliding Window (Fixed Size)  
**Language:** Python

---

## 🧠 Problem Overview

Given a string `s` and an integer `k`, find the **maximum number of vowels** in any substring of length `k`.

---

## 🔹 Approach 1: Brute Force (Baseline)

### Idea
- Generate every substring of length `k`
- Count vowels for each substring
- Track the maximum count

### Why it’s inefficient
- Recounts vowels again and again
- Time complexity becomes expensive for large inputs

### Complexity
- **Time:** `O(n × k)`
- **Space:** `O(1)`

```python
# Brute Force Approach
s = "abciiidef"
k = 3
max_count = 0

for i in range(len(s)):
    v = s[i:i+k]
    count = 0
    for ch in v:
        if ch in "aeiou":
            count += 1
    max_count = max(count, max_count)

print(max_count)
````

---

## 🔹 Approach 2: Sliding Window (Optimal)

### Idea

Instead of recalculating vowels for every substring:

* Create an **initial window of size `k`**
* Count vowels in this window
* Slide the window one character at a time:

  * ➕ Add vowel if new character enters
  * ➖ Remove vowel if old character leaves
* Update `max_count` at each step

Each character is processed **only once**.

---

### Why Sliding Window Works

* Avoids repeated work
* Maintains running count
* Perfect for fixed-size substring problems

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

```python
# Sliding Window (Optimal)
def maxVowels(self, s: str, k: int) -> int:
    vowels = "aeiou"
    count = 0

    # Initial window
    for i in range(k):
        if s[i] in vowels:
            count += 1

    max_count = count

    # Slide the window
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1

        max_count = max(count, max_count)

    return max_count


s = "abciiidef"
k = 3
print(maxVowels(0, s, k))
```

---

## ✅ Key Learnings from Day 3

* Sliding Window avoids unnecessary recomputation
* Each character enters and leaves the window **only once**
* Fixed-size window problems become simple once the pattern is clear
* Optimization is often about **rethinking the process**, not adding complexity

---

## 📌 Takeaway

> Don’t brute force what you can maintain smartly.

Day 3 done ✔️
Moving ahead with **more Sliding Window problems** 🚀

---

## 🔗 Repository

👉 **Full code on GitHub:**
[https://github.com/DevDoshi19/DSA_ProblemSolving](https://github.com/DevDoshi19/DSA_ProblemSolving)

---

### Tags

`#DSA` `#SlidingWindow` `#ProblemSolving` `#Python` `#LearningInPublic` `#Consistency`

