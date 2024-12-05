with open("input.txt","r") as file:
    data = file.read().splitlines()

def safe_unsafe(data):
    result = []
    for line in data:
        split = line.split()
        decr = False
        encr = False
        decr_reverse = False
        encr_reverse = False
        safe = True
        safe_reverse = True
        removed = False
        removed_reverse = False
        print(split)
        safes = []
        reverse = list(reversed(split))
        i = 0  # Índice manual
        while i < len(split) - 1:
            difference = int(split[i]) - int(split[i + 1])
            if i == 0:
                if difference < 0 and abs(difference) <= 3:
                    decr = True
                elif difference > 0 and abs(difference) <= 3:
                    encr = True
                else:
                    if removed:
                        safe = False
                        break
                    else:
                        removed = True
                        split.pop(i + 1)
                        continue
            else:
                if difference < 0 and abs(difference) <= 3:
                    if encr:
                        if removed:
                            safe = False
                            break
                        else:
                            removed = True
                            split.pop(i + 1)
                            continue
                elif difference > 0 and abs(difference) <= 3:
                    if decr:
                        if removed:
                            safe = False
                            break
                        else:
                            removed = True
                            split.pop(i + 1)
                            continue
                else:
                    if removed:
                        safe = False
                        break
                    else:
                        removed = True
                        split.pop(i + 1)
                        continue
            i += 1  # Avançar o índice somente se nada foi removido
        if safe:
            safes.append(line)
        result.append(safe)

        i=0
        while i < len(reverse) - 1:
            difference = int(reverse[i]) - int(reverse[i + 1])
            if i == 0:
                if difference < 0 and abs(difference) <= 3:
                    decr_reverse = True
                elif difference > 0 and abs(difference) <= 3:
                    encr_reverse = True
                else:
                    if removed_reverse:
                        safe_reverse = False
                        break
                    else:
                        removed_reverse = True
                        reverse.pop(i + 1)
                        continue
            else:
                if difference < 0 and abs(difference) <= 3:
                    if encr_reverse:
                        if removed_reverse:
                            safe_reverse = False
                            break
                        else:
                            removed_reverse = True
                            reverse.pop(i + 1)
                            continue
                elif difference > 0 and abs(difference) <= 3:
                    if decr_reverse:
                        if removed_reverse:
                            safe_reverse = False
                            break
                        else:
                            removed_reverse = True
                            reverse.pop(i + 1)
                            continue
                else:
                    if removed_reverse:
                        safe_reverse = False
                        break
                    else:
                        removed_reverse = True
                        reverse.pop(i + 1)
                        continue
            i += 1  # Avançar o índice somente se nada foi removido
        if safe_reverse:
            if not safes.__contains__(line):
                result.append(safe_reverse)
        else:
            result.append(safe_reverse)
    return result

count = 0
for a in safe_unsafe(data):
    if a:
        count+=1

print(count)
