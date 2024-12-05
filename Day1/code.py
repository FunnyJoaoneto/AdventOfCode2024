left = []
right = []
distance = 0

with open("input.txt","r") as file:
    data = file.read().splitlines()

for line in data:
    split = line.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

left.sort()
right.sort()

for i in range(len(left)):
    distance += abs(left[i]-right[i])

print(distance)

def recursion_iterative(left, right):
    total = 0
    for var1 in left:
        count = right.count(var1)
        total += count * var1
    return total

print(recursion_iterative(left,right))