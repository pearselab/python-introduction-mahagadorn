#M.A. Hagadorn
#November 21, 2016

#Bubble Algorithm:
#Think about it like the bubbles in a non-beer beverage.
#We want it to sort numbers lowest to highest.

def bubbles(to_sort, ascending):
    l = to_sort
    if ascending==True:
        for i in range(0, len(l)-1, -1):
        #range= (start, stop, step)
        #the above line is saying for some index in the range of staring position
        #length of our list minus one to the stopping position 0 (no more values in list
        #that haven't been examined), by increments that decrease by one.
            for j in range(i): #WAS PREVIOUSLY MISSING THIS LINE!
            #without this the numbers weren't sorting they were simply returning original list
            #What this is saying is for the jth value (our second index) in the range of our ith values apply the following blocks
            #it makes sense to add this because without it we aren't aren't taking in consideration the range of our values for the indexer "i"
                if l[i] < l[i+1]:
                    #saying if the index of "l" is less than the index plus one
                    #talk with Will about this?  Does this infact specify i + (one pisition) or the number of index plus one
                        #now we want to take advantage of python being able to process the following syntax
                        # def swap(x, y):
                        # x, y = y, x
                        # return x, y
                        l[i], l[i+1] = l[i+1], l[i]
                        #So here we are saying:
                        # if the subsetted index is less than the subsetted index plus 1 position
                        #Then I want you to swap these two values
                        #so l[i] and l[i+1] flip spot
    elif ascending==False:
        for i in range(len(l)-1, 0, 1):
            for j in range(i):
                if l[i] < l[i+1]:
                    l[i], l[i+1] = l[i+1], l[i]
        #this is working
    return l

x = [1,20,5,8,11]
### NEED TO LOOK AT IT IT DOESNT RETURN ASCENDING VS DESCENDING
#ONLY DOES BOTH DESCENDING
#SOMETHING WRONG WITH THE SYNTAX IN MY RANGE FOR THE ASCENDING PART?
