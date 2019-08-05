# Python 3 code to demonstrate Outputs for 
# SHA hash algorithms. 

import hashlib 

# initializing string 
str = "674e3fb360425e72f9af7c743a7b9427bdde503685a3d6dafa08957c0582ff8196528377260970178520"

# encoding Vivek1248 using encode() 
# then sending to SHA256() 
result = hashlib.sha256(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "Vivek1248"

# encoding Vivek1248 using encode() 
# then sending to SHA384() 
result = hashlib.sha384(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA384 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "Vivek1248"

# encoding Vivek1248 using encode() 
# then sending to SHA224() 
result = hashlib.sha224(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA224 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "Vivek1248"

# encoding Vivek1248 using encode() 
# then sending to SHA512() 
result = hashlib.sha512(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA512 is : ") 
print(result.hexdigest()) 

print ("\r") 

# initializing string 
str = "Vivek1248"

# encoding Vivek1248 using encode() 
# then sending to SHA1() 
result = hashlib.sha1(str.encode()) 

# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 is : ") 
print(result.hexdigest()) 
