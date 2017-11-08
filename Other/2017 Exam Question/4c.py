l = [[1,5,7,12],
    [3,4,15,16],
    [0,0,1,3],
    [12,16,18,23]]




for j in range(len(l)):
    total = 0 
    for i in range(len(l)):
       total += l[i][j]
    print(total/len(l))
    