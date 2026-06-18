#Write a program to Calculate sum of first N

i = int(input("ENTER YOUR NUMBER: "))

for num in range(1, i + 1):
    sum = 0
    sum += num + i
    
print("The sum of first", i, "numbers is:", sum)

