for x in range(151):
    print(x)

for x in range(0,1001,5):
    print(x)

for x in range(101):
    if x % 5 ==0:
        print("Coding")
    if x % 10 ==0:
        print("Dojo")
    else:
        print(x)

sum = 0
for x in range(500001):
    if x % 2 != 0:
        sum += x
print(sum)

for x in range(2018, 0,-4):
    print(x)

lowNum = 4
highNum= 48
mult= 5
for x in range(lowNum,highNum):
    if x % mult == 0:
        print (x)