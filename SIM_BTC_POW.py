#SImulating BTC Proof Of Work Using Python Code
import string
import random
import hashlib
import time

example_challange = 'hshcbb880eb44bckjb77'

def generation(challange=example_challange, size=20):
	answer = ''.join(random.choice(string.ascii_lowercase +
								   string.ascii_uppercase +
								   string.digits) for x in range(size))
	
	attempt = challange+answer

	return attempt, answer
#generation()
	


def testAttempt():
	Found = False
	start = time.time()	
	
	while Found == False:
		attempt, answer = generation()
		result = hashlib.sha256(attempt.encode())
		str = result.hexdigest()
		if str.startswith('000000'):
			print(str)
			Found = True
	print(answer)
	Timetook = time.time() - start
	print("Total Time taken:",Timetook)


testAttempt()
