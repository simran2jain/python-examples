# your code goes here
import string
import random

# initializing size of string
N = 7
result = ""
# using random.choices()
# generating random strings
for i in range(1000,1100,1):
	res = str(i)
	result = result + res + "\n"

with open("myfile.txt", "w") as file1:
    file1.write(result)
    file1.close()


