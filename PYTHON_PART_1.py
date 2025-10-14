
"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.


import math as mt

def divisible_by_7_not_multiple_of_5(start,end):

    for x in range(start,end+1,1):

        if(x%7==0 and float(mt.ceil(x/5)-x/5)!=0): # x % 5 != 0 the remainder isn't 0

            print(x)


divisible_by_7_not_multiple_of_5(2000,3200)


Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

import ipdb


def factorial_of_number(num):
  #ipdb.set_trace()

  if (num == 0):

    return 1

  else:

    return num * factorial_of_number(num-1)

factorial_of_number(8)

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}



def dictionary_of_number(num):

  dictionary = {}
  index = 0

  while index <= num:

    dictionary.update({index:index*index})

    index += 1

  return dictionary

print(dictionary_of_number(10))


Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

import ipdb as c
import keyboard

def make_this_text_caps_on():


  list_cap_off = []
  text = ""

  while True:

    #c.set_trace()
    text = input("write line of text | press (/s) key to quit")

    if text == "/s":
      break

    else:
      list_cap_off.append(text)


  for line in list_cap_off:

    print(line.upper())

  return "\n"

print(make_this_text_caps_on())


Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
"""
def compute_word_frequency(text):

  # ord should be used later on, now we gotta find a way to break a string to words

  letter_accumulator = ""
  word_list = {}

  for letter in text:
    
    letter_accumulator += letter

    if ord(letter)==32:
      
      word_list[letter_accumulator] = word_list.get(letter_accumulator, 0) + 1
      letter_accumulator = ""

  for key, value in word_list.items():
    print(f"{key}:{value}")
  
compute_word_frequency("If If If If you’re you’re you’re looking for free English books online, either in PDF or e-reader formats, start with classic literature: People have enjoyed these books for a long time, and they still enjoy them today. They contain themes and topics that are relevant to every human being, no matter whether they were born in 1600, 1950 or 2010")
