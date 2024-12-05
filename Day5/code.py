from time import perf_counter_ns

with open("input.txt","r") as file:
    data = file.read().splitlines()

rules={}
ordered=[]

start_dolist = perf_counter_ns()

for line in data:
    if "|" in line:
        spliting = line.split("|")
        first = int(spliting[0].strip())
        last= int(spliting[1].strip())
        if first in rules:
            rules[first].append(last)
        else:
            rules[first] = [last]

    else:
        spliting = line.split(",")
        if len(spliting)>1:
            ordered+=[[int(number.strip()) for number in spliting]]

time_list = round((perf_counter_ns() - start_dolist),2) / 1e6

def check_rules_order(rules,ordered):
    final= []
    for order in ordered:
        for number in order:
            if number in rules:
                rule = rules[number]
                index = order.index(number)
                if any(r in order[:index] for r in rule):
                    if order in final:
                        final.remove(order)
                    break
                else:
                    if order not in final:
                        final.append(order)

    return final

start_p1 = perf_counter_ns()


end = check_rules_order(rules,ordered)

total=0
for l in end:
    rah = l[int(len(l)//2)]
    total+=rah

print(total)
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")
print("Time taken + do list:", time_p1 + time_list, "ms")


#------------------Part2------------

start_p1 = perf_counter_ns()

notorder = [r for r in ordered if r not in end ]

def fix_notorder(rules, goats):
    final = []
    for order in goats:
        i=0
        while i < len(order):
            number = order[i]
            if number in rules:
                rule = rules[number]
                index = order.index(number)
                if any(r in order[:index] for r in rule):
                    for x in order[:index]:
                        if x in rule:
                            order.remove(x)
                            order.append(x)
                            i-=1
            i+=1
        final.append(order)
    return final


end2 = fix_notorder(rules,notorder)


total2=0
for l2 in end2:
    rah2 = l2[int(len(l2)//2)]
    total2+=rah2

print(total2)
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")
print("Time taken + do list:", time_p1 + time_list, "ms")