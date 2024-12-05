from time import perf_counter_ns

with open("input.txt","r") as file:
    data = file.read().splitlines()

start_p1 = perf_counter_ns()

board = []
count=0
for line in data:
    board += [list(line)]

def xmas(pos,next):
    dir = [next[0]-pos[0],next[1]-pos[1]]
    if any(abs(arg) >=2 for arg in dir):
        return 0
    if (next[0] + 2*dir[0] < 0 or next[0] + 2*dir[0] >= len(board) or next[1] + 2*dir[1] < 0 or next[1] + 2*dir[1] >= len(board[x])):
        return 0
    if data[next[0] + dir[0]][next[1] + dir[1]] == "A" and data[next[0] + 2*dir[0]][next[1] + 2*dir[1]] == "S":
        return 1
    return 0

total=0
row =0
maxrowcount = len(board)
while row < maxrowcount:
    col= 0
    maxcolcount = len(board[row])
    while col < maxcolcount:
        if board[row][col] == "X":
            for x in range(row-2,row+2):
                for y in range(col-2,col+2):
                    if x<0 or y<0 or x >= maxrowcount or y >= maxcolcount:
                        continue
                    if x==row and y==col:
                        continue
                    if board[x][y] == "M":
                        total += xmas([row,col],[x,y])

        col+=1
    row+=1

print(total)
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")


#-------------------Part2--------------------

start_p1 = perf_counter_ns()

board = []
count=0
for line in data:
    board += [list(line)]

def mas(pos):
    x,y = pos[0],pos[1]

    d1 = [x-1,y-1,x+1,y+1]
    d2 = [x+1,y-1,x-1,y+1]
    fd1 = False
    fd2 = False
    if (board[d1[0]][d1[1]] == "M" and board[d1[2]][d1[3]] == "S") or (board[d1[0]][d1[1]] == "S" and board[d1[2]][d1[3]] == "M"):
        fd1 = True
    if (board[d2[0]][d2[1]] == "M" and board[d2[2]][d2[3]] == "S") or (board[d2[0]][d2[1]] == "S" and board[d2[2]][d2[3]] == "M"):
        fd2=True
    if fd1 and fd2:
        return 1
    return 0

total=0
row =0
maxrowcount = len(board)
while row < maxrowcount:
    col= 0
    maxcolcount = len(board[row])
    while col < maxcolcount:
        if board[row][col] == "A":
            if row-1 < 0 or row +1 >=maxrowcount or col<0 or col+1 >=maxcolcount:
                col+=1
                continue
            else:
                total += mas([row,col])
        col+=1
    row+=1

print(total)
time_p1 = round((perf_counter_ns() - start_p1),2) / 1e6
print("Time taken:", time_p1, "ms")
