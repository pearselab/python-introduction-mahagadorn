## MAHagadorn
## Intro to python assignment
## November 16, 2016

##Getting into python interpreter via command line
#use > python3
#This will allow you to work in python3 through command line
#Mallorys-MacBook-Pro:python-introduction-mahagadorn Mal$ python3 intro.py


## 1. Write a loop that prints out the numbers from 20 to 10
#range will print from 0 to the maximum numbers
# third position is step(what to go by 1's,2's,3's) "-" means to make it go backwards
# first tried for i in range(20, 10, -1); doesn't work only prints to 11.
#Need to make the range from 20 to 9

numbST20 = []
for i in range(20, 9, -1):
    numbST20.append(i)
    print(i)



## 2. Write a list comprehension that returns the numbers from 20 to 10
#List Comprehension is a much quicker way of doing things (instead of looping)

numb_faster = [i for i in range(20, 9, -1)]


## 3. Write a loop that prints out only the numbers from 20 to 10 that are even.
#by making it -2 we will make it step backwards by TWO's!!! giving us the evens.

even_numb = []
for i in range(20, 9, -2):
    even_numb.append(i)
    print(i)


## 4. Write a list comprehension that prints out only the numbers from 20 to 10 that are even
#convert the above loop to list comprehension format

even_faster = [i for i in range(20, 9, -2)]


## 5. Write a function that calculates whether a number is a prime number
## (hint: what does 2 % 3 give you?)

def prime (x):
    for i in range(x-1, 2 , -1):
        if x < 2:               #if x is less than 2 return false: not prime
            return False
        elif x == 4:            #for some reason it kept giving me four as prime, so I added this elif statment
            return False
        elif x % i == 0:        #if the remainder of anything along the range is 0 its false: aka divisible by more than itself and one
            return False
    return True                 #the rest would be prime so return true

prime(5)
prime(2)
prime(20)



 #Mal, like a moron you spent about a hour trouble shooting stupid mistakes
 #You kept getting syntax errors: this is because you kept forgetting the : after loops
 #Also, note to self indent returns
 #Note to self 2, make sure your final return is at the same indentation as you first loop



## 6. Write a function that loads a text file, loops over the lines in it, and prints out the
#fifth character on the fifth line of that file.

#“Hint” (really, frankly, this is the solution):
#with open("name_of_file") as handle:
#for line in handle:
#Do something


#This does not work it give your call content
# def char_five (file_name):
#      with open('file_name', 'rt') as input_file: #open() reads in text file; 'rt'=open file as read text data
#         content = input_file.read()
#         print(content)
#         ###THIS PRINTS ALL CONTENT!
#I have fixed this below

#Working Good
def char_five (file_name):
    x = file_name
    with open(x) as input_file:
        for n, line in enumerate(input_file.readlines()):
            if n == 4:
                print (line[4])

char_five('Question6_Py1.txt')


###This is working. Let's talk about how you fixed the issue.
#Enumerate gives you the line number and the line that corresponds to that number
# EX. 1) Text
#My mistake is that I was trying to subset line twice
# n==4 & line==4
# SOOOO by simply calling the line by saying n==4 we get the text there too
#Then we subset line[at the appropriate positon]




## 7. Write a loop that prints out the numbers from 1 to 20, printing “Good: NUMBER” if the number is
#divisible by five and “Job: NUMBER” if then number is prime, and nothing otherwise.

#This works great: as per Will suggestion I translated his "perfect R code" to python.
#That's easy when you have good code to convert! Thanks, Will. :)

for each in range(1, 20, 1):
    if prime(each):
        print("Job: ", each)
    if (each % 5)==0:
        print("Good: ", each)



##8 A biologist is modelling population growth using a Gompertz curve, which is defined as y(t) = a.e−b.e−c.t
# where y is population size, t is time, a and b are parameters, and e is the exponential function. Write
# them a function that calculates population size at any time for any values of its parameters.

#This works, again used Will's code for inspiration
#Returns populations size based on the values of arguments

def gompertz (a, b, c, t):
    return a **(-b**(-c * t))
gompertz(2,3,4,5)
