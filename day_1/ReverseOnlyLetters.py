# Reverse Only Letters
string = "a-bC-dEf-ghIj"
s_list = list(string)
left , right = 0 , len(s_list) - 1

while left<right:
    if not s_list[left].isalpha():
        left +=1
    if not s_list[right].isalpha():
        right -=1
    else:
        s_list[left],s_list[right] = s_list[right] ,s_list[left]
        left +=1 
        right -= 1 

result = "".join(s_list)
print(result)
