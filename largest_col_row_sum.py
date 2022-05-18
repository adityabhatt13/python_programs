from sys import stdin

def findLargest(arr, nRows, mCols):

    sum_col = 0
    max_row = -1
    max_row_index = -1
    max_col = -1
    max_col_index = -1
    for i in range(nRows):
        sum_row = 0
        for j in range(mCols):
            sum_row += mat[i][j]
            if sum_row > max_row:
                max_row = sum_row
                max_row_index = i
    for j in range(mCols):
        sum_col = 0
        for i in range(nRows):
            sum_col += mat[i][j]
            if sum_col > max_col:
                max_col = sum_col
                max_col_index = j
        print("row 0 -2147483648")
    if max_row > max_col:
        print("row",max_row_index, max_row)
    else:
        print("column",max_col_index, max_col)                

def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1