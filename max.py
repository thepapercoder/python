import re
import sys
import random

def max(x, y):
	if x > y:
		return x
	else :
		return y

def ex2(a):
	b = a.lower()
	if re.search("[aeiou]", b):
		return True
	return False

def ex3(str):
	if str == str[::-1]:
		return True
	else:
		return False

def ex4(hlist):
	for element in hlist:
		print '*'*element

def ex5(wlist):
	i = []
	for word in wlist:
		i.append(len(word));
	return i

def ex6(filename):
	for line in open(filename,'r'):		
		line = line.replace(" ","").replace(",","").upper().replace("\n", "")
		if line == line[::-1] and len(line) > 0:
			print line

def ex7():
	num = random.randint(1,20)
	count = 0
	max_try = 5

	print "Hello! What is your name?"
	name = raw_input(">>>")

	while True:
		count+=1
		print "Well, %s, I am thinking of a number between 1 and 20" % (name)
		guess = int(raw_input("Enter a number: "))
		if guess == num:
			print "Good job ",count," is what you needed"
			return
		if guess > num: 
			print "Too high"
		elif guess < num:
			print "Too low"
	
def ex8():
	arr = []
	for i in range(1, random.randint(2, 20)):
		ran_int = random.randint(0,1)
		if ran_int == 1:
			arr.append("[")
		elif ran_int == 0:
			arr.append("]")
	print arr
	print ""
	
	stack = []
	for i in arr:
		if(i == "["):
			stack.append(i)
		elif len(stack) != 0:
			stack.pop()
	if len(stack) == 0:
		print "OK"
	else:
		print "NOT OK"
