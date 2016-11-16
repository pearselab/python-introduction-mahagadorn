## MAHagadorn
## Intro to python assignment
## November 16, 2016

##Getting into python interpreter via command line
#use > python3
#This will allow you to work in python3 through command line


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
    for(i in range((x-1),2, -1)
        r = (x % i)
        if(x < 2)
            return(Not Prime)
        if(r == 0)
            return(Not Prime)
        else
            return(Prime!)
