# Enter the number
a = int(input("enter the value of a :"))

# set the value of a into another variable
var = a if a % 2 == 1 else (a - 1)

i=0
while (var):
    i += 1
    if i % 2 == 1:
        var -= 1
        print(i, end=" ")
print()
