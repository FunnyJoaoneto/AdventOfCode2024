from time import perf_counter_ns

with open("input.txt","r") as file:
    data = file.read()

info = {}
info1 =[]

#print(data)
final = []

i = 0
count = 0
while i < len(data):
    if i%2==0:
        info[count] = int(data[i])
        count+=1
    else:
        info1.append(data[i])
    i+=1

last_added = count-1

def write(number,id,res):
    i=0
    while i < number:
        res+=str(id)
        final.append(id)
        i+=1
    return res

#print(info)
#print(info1)


end = ""
pop = 0
popping = -1

total = 0

while info:
    if pop == 0:
        id, number = next(iter(info.items()))
        del info[id]
        end = write(number,id,end)
        pop = info1.pop(0)
        pop = int(pop)
    #print(id, number)
    #print(info)
    if info:
        popping = info[last_added]
        new_id = last_added
        del info[last_added]
        last_added -= 1
        #print(f"pop ---------- {pop}         {popping}   {new_id}")
        if popping > pop:
            last_added += 1
            end = write(pop, last_added, end)
            info[last_added] = popping - pop
            pop = 0
        elif popping == pop:
            end = write(pop, last_added + 1, end)
            pop=0
        else:
            pop = pop - popping
            end = write(popping, last_added + 1, end)
    #print(info)
    #print(end)
total =0
i=0
while i < len(final):
    total+=i*final[i]
    i+=1
print(total)

#193390736206356
#23731748802322
#6242766523059 (right answer)
    
# ----------------------- Part2 ------------------------

end = ""
pop = 0
popping = -1
final2 = []
total = 0

info = {}
info1 =[]

i = 0
count = 0
while i < len(data):
    if i%2==0:
        info[count] = int(data[i])
        count+=1
    else:
        info1.append(data[i])
    i+=1

def write2(number,id,res):
    i=0
    while i < number:
        res+=str(id)
        final2.append(id)
        i+=1
    return res

while info:
    if pop == 0:
        id, number = next(iter(info.items()))
        del info[id]
        end = write2(number,id,end)
        pop = info1.pop(0)
        pop = int(pop)
    #print(id, number)
    #print(info)
    if info:
        popping = info[last_added]
        new_id = last_added
        del info[last_added]
        last_added -= 1
        #print(f"pop ---------- {pop}         {popping}   {new_id}")
        if popping > pop:
            ola=1
        elif popping == pop:
            end = write2(pop, last_added + 1, end)
            pop=0
        else:
            pop = pop - popping
            end = write2(popping, last_added + 1, end)
            end = write2(pop,".",end)
            pop=0
    #print(info)
    #print(end)
total =0
i=0
while i < len(final2):
    total+=i*final2[i]
    i+=1
print(total)
