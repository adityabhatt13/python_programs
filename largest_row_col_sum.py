def largest_row_sum(li):
    n = 3
    m = 4
    max_row_sum = -1
    for i in range(n-1):
        sum = 0
        for j in range(m-1):
            sum = sum + li[i][j]
        print(sum, end =" ")   

            



# def largest_col_sum(li):


li = [[1,2,3],[4,5,6],[7,8,]]
max_row_sum = largest_row_sum(li)
# max_col_sum = largest_col_sum(li)