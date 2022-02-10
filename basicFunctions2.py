""" #Problem 1. 
list= []
def countdown(num):
    for x in range(num,-1,-1):
        list.append(x)
        print(list)
print(countdown(5))


#Problem 2
def printAndReturn(a,b):
    print(a)
    return b
print(printAndReturn(1, 5))
"""
# Problem 3
list = [3,6,9,12]
def firstPlusLength(list):
    a= list[0]
    b= len(list)
    print (a, b, a+b)
firstPlusLength(list)