"""
t = (2,1,4,6,2,1,4,1,2,7,1)
Q1.write the code to count the frequency of 1
Q2.write a code to merge tuple t with (11,12,13,14) & store in variable named newt
"""

t= (2, 1, 4, 6, 2, 1, 4, 1, 2, 7, 1)
# Q1: Method 1
count= 0
for i in t:
    if i == 1:
        count += 1
print("Frequency of 1 in tuple is " + str(count))

# Q1: Method 2

print("Frequency of 1 in tuple is", t.count(1))

# Q2:
newt= t + (11, 12, 13, 14)
print(newt)
