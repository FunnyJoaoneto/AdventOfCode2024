from time import perf_counter_ns
import re

start_p1 = perf_counter_ns()

def check_regex(text):
    # Define the regex pattern
    pattern = r"^mul\((\d{1,3}),(\d{1,3})\)$"

    match = re.match(pattern, text)

    if match:
        return True, (int(match.group(1)), int(match.group(2)))
    else:
        return False, None
    
    
with open("input.txt","r") as file:
    data = file.read()

i = 0
total = 0
while i < len(data):
    if data[i]=="m":
        mul = data[i:i+12]
        index = mul.find(")")
        if index != -1:
            valid, numbers = check_regex(mul[:index+1])
            if valid:
                total += numbers[0]*numbers[1]
            i+=index
    i+=1

print(total)
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")



# ------------- Part 2 -------------------

start_p2 = perf_counter_ns()

def check_do(text):
    if text == "do()":
        return 1
    elif text == "don't()":
        return 0
    else:
        return -1
    

i = 0
total = 0
do = True
while i < len(data):
    if data[i]=="d":
        enabled = data[i:i+7]
        index = enabled.find(")")
        if index != -1:
            validation = check_do(enabled[:index+1])
            if validation == 1:
                do = True
                i+=index
            elif validation ==0:
                do = False
                i+=index
            else:
                print("ignora")
    if do:
        if data[i]=="m":
            mul = data[i:i+12]
            index = mul.find(")")
            if index != -1:
                valid, numbers = check_regex(mul[:index+1])
                if valid:
                    total += numbers[0]*numbers[1]
                    i+=index
    i+=1

print(total)
time_p2 = round((perf_counter_ns() - start_p2),2) / 1e6
print("Time taken:", time_p2, "ms")