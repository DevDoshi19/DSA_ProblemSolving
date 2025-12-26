# Maximum Number of Vowels in a Substring of Given Length
# Brute Force Approach
s="abciiidef"
k = 3
max_count = 0
for i in range(len(s)) :
    v = s[i:i+k]
    count = 0
    for i in v:
        if i == "a" or i =="e" or i =="i" or i == "o" or i == "u":
            count +=1
            
    max_count = max(count,max_count) 
            
print(max_count)

# Sliding Window Approach
# Optimal Solution
def maxVowels(self, s: str, k: int) -> int:
    vowels = "aeiou"
    count = 0
        
    for i in range(k):
        if s[i] in vowels :
            count += 1
        
    max_count = count

    for i in range(k,len(s)):
        if s[i] in vowels:
            count += 1 
        if s[i-k] in vowels :
            count -= 1
            
        max_count = max(count,max_count)

    return max_count

s = "abciiidef"
k = 3
print(maxVowels(0,s,k))
