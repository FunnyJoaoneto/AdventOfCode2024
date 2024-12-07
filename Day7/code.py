from time import perf_counter_ns
from itertools import product

with open("input.txt","r") as file:
    data = file.read().splitlines()

start_p1 = perf_counter_ns()


equations = {
    int(line.split(":")[0]): list(map(int, line.split(":")[1].split()))
    for line in data
}

symbols = ["*", "+"]

end = []


for result, equation in equations.items():
    size = len(equation)-1
    combinations = list(product(symbols, repeat=size))
    for combo in combinations:
        res = 0
        i=0
        while i < len(combo):
            if i == 0:
                res = equation[i]
            if combo[i] == "*":
                res *= equation[i+1]
            elif combo[i] == "+":
                res += equation[i+1]

            if res > result and equation[i+1] !=1:
                break

            i+=1
        if res == result:
            end.append(res)
            break

total=0
for a in end:
    total+=a

print(total)

time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")


#-----------------Part2----------------------

start_p1 = perf_counter_ns()

symbols = ["*", "+", "||"]

end1 = []
concs = []


for result, equation in equations.items():
    if result in end:
        continue
    size = len(equation)-1
    combinations = list(product(symbols, repeat=size))
    for combo in combinations:
        if "||" in combo:
            new_res = 0
            i=0
            while i < len(combo):
                if new_res == 0:
                    new_res = equation[i]
                if combo[i] == "*":
                    new_res*=equation[i+1]
                elif combo[i] == "+":
                    new_res+=equation[i+1]
                elif combo[i] == "||":
                    new_res = int(str(new_res) + str(equation[i + 1]))
                i+=1

            if new_res == result:
                end1.append(new_res)
                break
total1=0
for b in end1:
    total1+=b

print(total+total1) #189207836795655

time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")