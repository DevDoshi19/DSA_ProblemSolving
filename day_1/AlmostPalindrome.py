# Check if a string can be made palindrome by removing at most one character
def isPalindrome(s,left,right):
    while left < right :
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True    

s = 'abcca'
left , right = 0 , len(s)-1

while left < right :
    if s[left] == s[right]:
        left += 1
        right -= 1
    else :
        print(isPalindrome(s,left+1,right) or isPalindrome(s,left,right-1)) 
        break   

