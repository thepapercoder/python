#!/usr/bin/python
## Solutions for exercises of Class 1

##imports:
import re
import random
import sys

## My functions:

def maximum(a,b): 
  """
  Solution for exercise 1
  author: G. Teixeira
  """  
  if a >= b:
    c = a
  else:
    c = b
  return c  

def vowels(b):
  """
  Solution for exercise 2
  author: G. Teixeira
  """  
  a = b.lower()
  if re.findall('a',a)!=[] or re.findall('e',a)!=[] or \
     re.findall('i',a)!=[] or re.findall('o',a)!=[] or re.findall('u',a)!=[]:
    return True
  else:
    return False

def vowels_alt(c):
  """
  Alternative Solution for exercise 2
  authour: S. Sousa
  """  
  if re.search("[aeiouAEIOU]",c):
    return True
  return False
	

#exercise3
def is_palindrome(str_to_test):
  """
  Solution for exercise 3
  authour: G. Teixeira
  """
  if str_to_test==str_to_test[::-1]:
    return True
  else:
    return False
    
#exercise4
def histog1(hlist):    
  """
  Solution for exercise 4
  author: G. Teixeira
  """  
  for element in hlist:
    print '*'*element
    
#exercise5
def mapper_for_classic(listword):
  """
  Solution for exercise 5a
  author: S. Sousa
  """  
  number_list = []
  for i in range(0,len(listword)):
    number_list.append(len(listword[i]))
  return number_list

def mapper_for(listword):
  """
  Solution for exercise 5b
  author: S. Sousa
  """  
  number_list=[]
  for word in listword:
    number_list.append(len(word))
  return number_list

def mapper_comp_list(listword):
  """
  Solution for exercise 5c
  author: S. Sousa
  """  
  return [len(word) for word in listword]

#exercise6
def palindromes_in_file(file_pal):
  """
  Solution for exercise 6
  author: S. Sousa
  """  
  for line in open(file_pal,'r'):
    line = line.strip()
    line_test = line.replace(",", "").replace(" ", "")
    if len(line_test) > 0 and is_palindrome(line_test.upper()):
      print line


#exercise7
def guesser():
  """
  Solution for exercise 7
  author: S. Sousa
  """  
  name=raw_input("Hello! What is your name?    ")
  number_to_guess = random.randint(1,20)
  trys = 5;     
  print "Well, ",name," , I am thinking of a number between 1 and 20."
  guess_counter = 1
  while guess_counter <= trys:
    number=int(raw_input("Take a guess!: "))
    if number == number_to_guess:
      print 'Good job %s! You guessed my number in %d guesses!' % (name,guess_counter)
      return
    if number > number_to_guess:
      print 'Your number is too High'
    else:
      print 'Your number is too low!'
    guess_counter += 1
  print 'You were not able to guess the number in less than %d .' % trys
  print 'You suck ',name,'!'  
  print 'I was thinking on the number ', number_to_guess


#exercise8
def generatebrack(n):
  """
  Solution for exercise 8
  This will generate a equal number of open and closed brackets
  author: S. Sousa
  """  
  brackets = '['*n + ']'*n
  brackets_test = ''
  sample_ind = random.sample(range(2*n),2*n)
  for ind in sample_ind:
    brackets_test += brackets[ind]
  print "Brackets to test: ", brackets_test

  test_count = 0
  for char in brackets_test:
    if char=='[':
      test_count += 1
    else:
      test_count -= 1
    if test_count < 0:
      print brackets_test, "    NOT OK"
      return      
#  if test_count == 0:
  print brackets_test, "     OK"
#  else:
#    print brackets_test, "     NOT OK"

  
  
### Main program:
def main():
  """
  Main program to test the exercises.
  Author: S. Sousa
  """  
  print "Hello"

# uncomment next 3 lines to test Exercise 1:  
#  a = float(raw_input('choose the first number: '))
#  b = float(raw_input('Input the second number: '))
#  print 'The maximum number is: ', maximum(a,b)

# uncomment next lines to test Exercise 2:
#  test_char = 'a'
##  if vowels(test_char):
#  if vowels_alt(test_char):
#    print test_char + ' is a vowel'
#  else:
#    print test_char + ' is not a vowel'


# uncomment next 4 lines to test Exercise 3. (must provide parameter to script)  
#  if len(sys.argv) == 2:
#    print palindrome(sys.argv[1])
#  else:
#    print "Need 1 parameters ex.: ./Exercises1.py testset"

# uncomment next 2 lines to test Exercise 4.
#  hlist=[1,5,3,4]
#  histog1(hlist)

# uncomment next lines to test Exercise 5.
#  listword=['blabla','bla','ret','a']
#  print 'Classic For             : ', mapper_for_classic(listword)
#  print 'Python For              : ', mapper_for(listword)
#  print 'Using Comprehension list: ', mapper_comp_list(listword)

# uncomment next lines to test Exercise 6. Need to have a file
#  palindromes_in_file('file_with_palindromes.txt')

# uncomment next line to test Exercise 7
#  guesser()


# uncomment next lines to test Exercise 8
#  generatebrack(5)


if __name__ == "__main__":
  main()

