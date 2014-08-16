#!/usr/bin/env python
import random

random_num = random.randrange(0,11,2)
i = 0
while True:
    user_input = raw_input("Please enter a number:")
    num = int(user_input)
    if num == random_num:
        print "You guessed it!"
        i += 1
        print "You guess %d times" % (i)
        break
    elif num < random_num:
        print "Your input number is too small, please input again!"
        i += 1
    else:
        print "Your input number is too big, please input again!"
        i += 1
