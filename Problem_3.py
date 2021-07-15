# Enter the Number for
num = int(input("enter the value of num :"))
# initialize two variables length and reverse as len ,and rev
len, rev = 0, False

# Set the condition

for i in range(num * 2 - 1):
    # check the given length is greater than number,the set reverse is true
    if len >= num:
        rev = True
    # if its not true then set i+1 in length
    if not rev:
        len = i + 1

    else:
        len -= 1
    #Check the condition
    if i % 2 == 0:
        for j in range(1, len + 1):
            print(j, end=" ")
    else:
        for j in range(len, 0, -1):
            print(j, end=" ")
    print()