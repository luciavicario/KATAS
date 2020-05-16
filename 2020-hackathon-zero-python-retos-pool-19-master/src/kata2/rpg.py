#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen = 10):
    total_posibilities = string.ascii_letters + string.digits + string.punctuation
    print (total_posibilities)

    password = ""
    for positions in range(passLen):
        password = password + random.choice(total_posibilities)
    
    #password = random.sample(total_posibilities,passLen)
    return password

password = RandomPasswordGenerator(10)
#password = ''.join(password)
print(password)
   