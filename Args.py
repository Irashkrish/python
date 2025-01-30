# In this program we learned about args
# *args are parameter that will pack all arguments into a tuple
#usefull so that a function can accept a varying amount of arguments


# example program

def add(*args):    #The asterisk symbol is very important 
    sum= 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3,4)

# To use indexing change tuple to list or any mutable object
#using type casting
