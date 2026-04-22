# print number 1 to 10 using while loop

num = 1
while num <= 10:
    print(num)
    num = num + 1


# print number 10 to 1 using while loop

i = 10
while i >= 1:
    print("i =", i)
    i = i - 1

# print even number between 1 to 50

even = 1
while even <= 50:
    if even % 2 == 0:
        print("Even Number is : ", even)
    even = even + 1


# print sum of  first natural number
natural = int(input("Enter Natural number"))
sum = 0
while natural >= 1:
    sum = sum + natural
    natural = natural - 1

print("Sum is : ", sum)
print("Natural is : ", natural)

# print star
# *
# * *
# * * *
# * * * *

n = 1
while n <= 4:
    print(" * " * n)
    n = n + 1


# print Multiplication table 1 to 10 of any number

table = int(input("Enter any Number"))
i = 1
while i <= 10:
    print(f"{table} * {i}={table*i}")
    i += 1
