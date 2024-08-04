def row_def(matrix,m,n):
    r=0
    for i  in range(m):
        for j in range(n):
            if (i==0 or i==m-1):
                da=matrix[i][j]
                r+=da   
    return r           

def col_def(matrix,m,n):
    r=0
    for i  in range(m):
        for j in range(n):
            if (0<i<m-1) and (j==0 or j==n-1):
                da=matrix[i][j]
                r+=da 
    return r            



m,n=map(int,input().split())
matrix=[]
for i in range(m):
    raw=list(map(int,input().split()))
    matrix.append(raw)
     
row=row_def(matrix,m,n)
call=col_def(matrix,m,n)
re=row+call 
print(re)







