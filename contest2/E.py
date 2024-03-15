def vagoni(poezd):
    tupik = []
    rez = []
    i = 1
    count = 0
    for j in poezd:
        if j != i:
            tupik.append(j)
            count += 1
        else:
            tupik.append(j)
            i+= 1
            rez.append([1, count + 1])
            count = 1
            tupik.pop()
            while tupik and tupik[-1] == i:
                i+= 1
                tupik.pop()
                count+= 1
            rez.append([2,count])
            count = 0
    if len(tupik) == 0:
        return rez
    else:
        return 0


n = int(input())
poezd = list(map(int,input().split()))
result = vagoni(poezd)
if result == 0:
    print(result)
else:
    print(len(result))
    for i in result:
        print(*i,sep = " ")