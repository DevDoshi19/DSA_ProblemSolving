#3 rd Method
def isPalindrome(self, x: int) -> bool:
    if x < 0 :
        return False
            
    else:
        s = str(x)
        left , right = 0 , len(s)-1
        while left < right :
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
    return  True 

x = 121
print(isPalindrome(0,x))
