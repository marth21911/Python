"""
#1 will return 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#2 will return error function undefined
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#3 will return 5, second return is never reached
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#4 will return 5, print statement is never reached
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#5 will return error, expected 1 arguement, recieved 0. I was wrong, it just assumed none 
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#6 I believe there will be an error from b and c being undefined and not strings. Correct.
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#7 print 25. Hmm. Didn't. I think because the return stores nothing, even though the print tries to do something the return cuts it off.
def concatenate(b,c):
    return str(b)+str(c)
    print(concatenate(2,5))

#8 I believe it willreturn 10, as 100 is greater than 10, which was the condition of the if/else. return 7 is not reached. 
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#9 It will print 7, 14, 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#10 will print 8, as second line ends function
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#11  print 500, print 300, 300, 300, 300. So the updated b value only exists in the function because it is never returned. 
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#12 print 500, print 500 (foobar hasnt been called yet!) print 300 print 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#13 print 500, print 500, print 300, print 300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#14  print 1 3 2 
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

"""
#15  1, 3, 5 , 10
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)











