import os

def isPalindrome(string):
    flag = True
 
    #if there are capital letters in the string, convert them into lowercase ones 
    string = string.lower();  
   

    for i in range(0, len(string)//2):  
        if (string[i] != string[len(string)-i-1]):
        
            flag = False
            break
    
    return flag
    
   
print('Write a string: ', end="")
string = input()

PalFlag = isPalindrome(string)

print('')
if PalFlag:
    print('The string is palindrome')
    
else:
    print('The string in NOT palindrome')

print('')
os.system('pause')