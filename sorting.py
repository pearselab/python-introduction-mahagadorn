#M.A. Hagadorn
#November 21, 2016





#Bubble Algorithm:
#Think about it like the bubbles in a non-beer beverage.
#We want it to sort numbers lowest to highest.

x = [1,20,5,8,11]

def bubbles(to_sort):
l = to_sort
    for i in range(len(l)-1, 0, -1)
    #range= (start, stop, step)
    #the above line is saying for some index in the range of staring position
    #length of our list minus one to the stopping position 0 (no more values in list
    #that haven't been examined), by increments that decrease by one.
    
