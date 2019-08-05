# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal) (A slight change in Source results abrupt Changes in Hash Values)

import hashlib 

# initializing string 
str = "My Name is vivek"
str1 = "My Name isvivek"
# encoding str1 and str2 using encode() 
# then sending to md5() 
result1 = hashlib.md5(str.encode())
result2 = hashlib.md5(str1.encode())
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of 1st string is : ", end ="")
print(result1.hexdigest())
print("The hexadecimal equivalent of 2nd string is : ", end ="")
print(result2.hexdigest())
