#MA Hagadorn
#Section 11
#Optimisation



#In this session we will be covering optimisation algorithms
#Today's algorithms were chosen because they underlie most numerical and statistical
#work that are likely to be carried out on a computer

#We will only be writing linear optimisation algorithms





#11.1 What is optimisation and why does it matter?
#Scientists often need to find the maximum and minimum of an equation
#This is because extremes reflect things that we need in the real world
#OPTIMISATION is the process by which we find those extreme values

#Numerical optimisation comes in to play when there are contraints to problems
##see hand out for calculus examples (calculus ughhh)
#If you can calculate an equation of interest given ANY set of input parameters
    #then you can use the algorithms we are going to write Today

#There are 2 main classes of optimisation algorithms
    #1. linear optimisation (work for a single dimension)
    #2. Multi-demensional  (work to optimise multiple dimensions simultaneously)

#Will's words of warning:
    #1. there are often multiple LOCAL optima
        #could lead to astray, thinking you found a global optima when you haven't
        #THIS IS WHY YOU NEED TO SEARCH FOR MULTIPLE STARTING POSITIONS
    #2. these algorithms assume your functions are mathmatically smooth
        #AKA
            #they are not random
            #slight changes in parameter values won't cause huge changes in output




#11.2 Bisection
#the simplest method for finding the solution to a linear problem
#here, we are trying to find where a certain function(equation) is equal to zero
#it's robust, but slow

# 1: Pick interval (a, b) over which to find minimum
# 2: Pick tolerance (t)
# 3: while (loop) f (c)− f (a) > t or f (c) > t do
# 4: Evaluate function at mid-point of interval (a, b)
# 5: Set a and b to (a,c) or (c,b) such that interval contains zero
# 6: End While loop
