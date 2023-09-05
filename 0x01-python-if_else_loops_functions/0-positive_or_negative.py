#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    result = "positive"
elif number == 0:
    result = "zero"
else:
    result = "negative"
print(f"{number} is {result}")
