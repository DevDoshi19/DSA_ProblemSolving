# 🚀 Day 1 – Problem Solving / DSA Journey

Today marks the **start of my DSA journey from the basics**, with a focused deep dive into the **Two Pointer technique**.

Instead of jumping into advanced problems, I’m intentionally building **strong fundamentals** and understanding **why a technique works**, not just how to code it.

---

## 🔹 Today’s Focus: Two Pointer Pattern (Basics)

All problems were solved using **Python**, with an emphasis on:

* clarity of logic
* correct pointer movement
* interview-friendly approaches

---

## 1️⃣ Remove Negatives (In-place Array Modification)

**Concept used:** Slow & Fast Pointers

* Slow pointer (`k`) tracks the position to place the next valid element
* Fast pointer (`i`) scans the array
* When a non-negative number is found, it overwrites the value at index `k`

💡 **Why Two Pointers?**
This approach avoids creating a new array and performs the operation **in-place**, making it both memory-efficient and interview-ready.

---

## 2️⃣ Reverse Only Letters

**Concept used:** Left & Right Pointers

* Left pointer starts from the beginning
* Right pointer starts from the end
* Non-letter characters are skipped
* Letters are swapped when both pointers point to valid characters

💡 **Key Insight:**
Pointers don’t always move symmetrically — they can **skip conditions intelligently**.

---

## 3️⃣ Pair With Given Sum (Sorted Array)

**Concept used:** Two Pointers on a Sorted Array

* Add values at `left` and `right`
* If the sum is too small → move `left`
* If the sum is too large → move `right`

💡 **Critical Rule:**
At least **one pointer must move in every iteration**, otherwise the logic fails.

---

## 4️⃣ Almost Palindrome

**Concept used:** Two Pointers with One Allowed Mistake

* Compare characters from both ends
* On the first mismatch, allow **one skip**:

  * skip left **or**
  * skip right
* If either remaining substring is a palindrome → return true

💡 **Learning:**
This problem highlights how to handle **controlled edge cases** without breaking the core logic.

---

## ✅ Key Takeaways from Day 1

* Two pointers can reduce **O(n²) → O(n)**
* Overwriting values is better than removing elements
* Pointer movement logic matters more than code length
* Strong fundamentals beat solving many problems fast

---

📌 **Starting small. Staying consistent. Prioritizing clarity over speed.**

➡️ **Next:** Sliding Window patterns 🚀

---

### Tags

`#DSA` `#ProblemSolving` `#TwoPointers` `#Python` `#LearningInPublic` `#Consistency`

