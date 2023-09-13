a= [[5,3,8,4],[3,8,7,1],[1,4,6,3]]
result=[]
for i in range(len(a)):
   for j in range(len(a[i])):
      if a[i][j]==7:
        result.append(i)
        result.append(j)
        print(result)    