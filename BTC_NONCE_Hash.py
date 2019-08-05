 #To test BTC Proof of work with Nonce
import string
import random
import hashlib
import time

example_challange = 'vivekshanbhag'

hash1 = hashlib.sha256(example_challange.encode()) 

# printing the equivalent hexadecimal value. 

hash2 = hash1.hexdigest()
print("The SHA256 hexadecimal equivalent of ",example_challange) 
print(hash2)


def generate(challange=hash2, size=20):
	answer = ''.join(random.choice(string.digits) for x in range(size))
	
	attempt = challange+answer

	return attempt, answer
#generate()
	


def testAttmpt():
	Found = False
	start = time.time()	
	
	while Found == False:
		attempt, answer = generate()
		result = hashlib.sha256(attempt.encode())
		str = result.hexdigest()
		if str.startswith('000v'):
			print(str)
			Found = True
	print(answer)
	Timetook = time.time() - start
	print("Total Time taken:",Timetook)


testAttempt()
