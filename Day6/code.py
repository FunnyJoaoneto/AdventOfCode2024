from time import perf_counter_ns

with open("input.txt","r") as file:
    data = [list(line) for line in file.read().splitlines()]

next_dir={
    "^":[0,-1],
    "v":[0,1],
    "<":[-1,0],
    ">":[1,0]
}

next_guard={
    "^":">",
    "v":"<",
    "<":"^",
    ">":"v"
}

maxy= len(data)
maxx=len(data[0])

guard = ["^","v","<",">"]

start=[]
yi=0
while yi < maxy:
        xi=0
        while xi < maxx:
            if data[yi][xi] in guard:
                start=[xi,yi]
                break
            xi+=1
        if start!=[]:
            break
        yi+=1

result = set()


def reach_end(pos):
    if pos[0]==0 or pos[0]==maxx-1 or pos[1]==0 or pos[1]==maxy-1:
        return True
    return False

def move(pos,dir):
    nx,ny = pos[0],pos[1]
    gx,gy = nx,ny
    while True:
        if data[ny][nx] == "#":
            return gx,gy
        result.add(f"{nx}_{ny}")
        if reach_end([nx, ny]):
            data[ny][nx] = "X"
            return nx,ny
        gx,gy = nx,ny
        data[gy][gx] = "X"
        nx+=dir[0]
        ny+=dir[1]


def game():
    gx,gy = start[0],start[1]
    gua = data[gy][gx]
    while not reach_end([gx,gy]):
        dir = next_dir.get(gua)
        gx,gy = move([gx,gy],dir)
        gua = next_guard.get(gua)

start_p1 = perf_counter_ns()

game()
print(len(result))

time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")


#-------------------- Part2 ----------------------------

start_p1 = perf_counter_ns()

data[start[1]][start[0]] = "^"

possibilities= []
count_obstacles = 0

yi=0
while yi < maxy:
    xi=0
    while xi < maxx:
        if data[yi][xi] == "X":
            possibilities.append([xi,yi])
        if data[yi][xi] == "#" and yi < maxy-1 and xi < maxx-1:
            count_obstacles+=1
        xi+=1
    yi+=1

max_moves = ((maxx-2) * (maxy-2)) - count_obstacles

def move2(pos,dir):
    nx,ny = pos[0],pos[1]
    gx,gy = nx,ny
    steps = 0
    while True:
        if data[ny][nx] == "#":
            steps-=1
            return gx,gy,steps
        if reach_end([nx, ny]):
            data[ny][nx] = "X"
            return nx,ny,steps
        gx,gy = nx,ny
        data[gy][gx] = "X"
        nx+=dir[0]
        ny+=dir[1]
        steps+=1

def check_loop():
    gx,gy = start[0],start[1]
    gua = data[gy][gx]
    count = 0
    while not reach_end([gx,gy]):
        dir = next_dir.get(gua)
        gx,gy,steps = move2([gx,gy],dir)
        gua = next_guard.get(gua)
        count+=steps
        if count > max_moves:
            return True
    return False

loop_count=0
for obstacle in possibilities:
    data[start[1]][start[0]] = "^"
    provx,provy = obstacle[0],obstacle[1]
    data[provy][provx] = "#"
    if check_loop():
        loop_count+=1
    data[provy][provx] = "X"

print(loop_count)
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")

