"""
Write a python to count number of odd and even number from the series in the list:
[2,3,4,55,56,78,75,69,66,101,100]
"""
list= [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]

even= []
odd= []

for i in list:
    if (i % 2 == 0):
        even.append(i)

    else :
        odd.append(i)

print("even numbers are " + str(even))
print("odd numbers are " + str(odd))
