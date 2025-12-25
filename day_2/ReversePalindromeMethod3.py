#3 rd Method
def isPalindrome(self, x: int) -> bool:
    if x < 0 :
        return False
            
    num = x 
    reverse_num = 0 
    while num > 0 : 
        digit = num % 10
        reverse_num =(reverse_num*10) + digit 
        num //= 10 

    return x == reverse_num 

x = 12134
print(isPalindrome(0,x))
