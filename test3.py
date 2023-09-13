arr2D=eval(input())
for i in range(len(arr2D)):
    for j in range(len(arr2D[i])):
        if arr2D[i][j]==7:
            arr2D[i][j]=8
            
print(arr2D)