<h1 align="left">🧠 Problem 9: Reverse Palindrome</h1>

<h3 align="left">
Exploring a single problem using <strong>multiple approaches</strong> to deeply understand
<strong>logic, optimization, and interview trade-offs</strong>.
</h3>

<br/>

<div align="center">
  <img height="180" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" />
</div>

---

## 🚀 Problem Statement

Given an integer, determine whether it is a **palindrome**  
(a number that reads the same forward and backward).

Instead of stopping at one solution, I implemented **3 different approaches** to understand:
- How logic evolves
- Why some solutions are more optimal
- Which approach is preferred in interviews

---

## 🔹 Method 1 — Two Pointer (String Based)

**Idea:**  
Convert the number into a string and compare characters from both ends.

**How it works:**
- Use `left` and `right` pointers
- Move inward while characters match
- Break immediately on mismatch

**Why this method matters**
- Very readable
- Easy to reason about
- Great for understanding pointer logic

**Complexity**
- Time: `O(n)`
- Space: `O(n)`

---

## 🔹 Method 2 — Reverse String Comparison

**Idea:**  
Reverse the string and compare it with the original.

**How it works:**
- Convert number → string
- Reverse using slicing `[::-1]`
- Compare both strings

**Why this method matters**
- Clean and Pythonic
- Minimal code
- Useful for quick checks

**Trade-off**
- Uses extra memory

**Complexity**
- Time: `O(n)`
- Space: `O(n)`

---

<div align="center">
  <img height="180" src="https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif" />
</div>

---

## 🔹 Method 3 — Mathematical Reversal (No String)

**Idea:**  
Reverse the number using pure math.

**How it works:**
- Extract digits using `% 10`
- Build reversed number using multiplication
- Compare reversed value with original

**Why this method matters**
- No string conversion
- Space efficient
- Most **interview-preferred**

**Complexity**
- Time: `O(n)`
- Space: `O(1)`

---

## ✅ Key Learnings

- Same problem can have **multiple valid solutions**
- Readability vs optimization is a **design choice**
- Math-based solutions show deeper understanding
- Two pointers reduce unnecessary comparisons

---

## 🎯 Final Thought

> Don’t memorize solutions.  
> Understand **why each approach works** and **when to use it**.

Building strong DSA fundamentals — one problem at a time 🚀

---

## 🔗 Let’s Connect

<div align="left">
  <a href="https://www.linkedin.com/in/dev-doshi-8360a727b" target="_blank">
    <img src="https://raw.githubusercontent.com/maurodesouza/profile-readme-generator/master/src/assets/icons/social/linkedin/default.svg"
         width="52" height="40" />
  </a>
</div>
