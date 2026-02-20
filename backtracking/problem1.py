# Rat in a Maze

mat = [[0,0,0,0,1],
       [0,1,1,0,0],
       [0,0,1,1,1],
       [0,0,0,0,0]]
path = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
#print(mat)

# 0 --> free cell
# 1 --> blocked cell
# movements allowed is right/down/diagonal

def rIAM(mat : list[list[int]], r : int, c : int, path, ct):
    path[r][c] = 1
    #base
    if r == len(mat) - 1 and c == len(mat[0]) - 1 :
        ct[0]+=1
        for i in range(0, len(path)):
            print(path[i])
        print()
        return False
    #rec
    #right
    if c+1 < len(mat[0]) and mat[r][c+1] == 0 and rIAM(mat, r, c+1, path, ct) : return True
    #down
    if r+1 < len(mat) and mat[r+1][c] == 0 and rIAM(mat, r+1, c, path, ct) : return True
    #diagonal
    if r+1 < len(mat) and c+1<len(mat[0]) and mat[r+1][c+1] == 0 and rIAM(mat, r+1, c+1, path, ct) : return True   
    path[r][c] = 0
    return False

ct = [0]
print(rIAM(mat, 0,0, path, ct))
print(ct[0])