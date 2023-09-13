a=[[1,2,3],[4,5,6]]
for i in a:
    number=" "
    for j in range(len(i)):
        number=number+str(i[j])+","
    print(number,end="")
                