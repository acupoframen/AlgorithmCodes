data=[list(input().split()) for _ in range(9)]
info={}
for i in range(3):
    for j in range(3):
        temp=[]
        name=0
        if i==j==1:
            continue
        for a in range(3):
            for b in range(3):
                if a==b==1:
                    name=data[3*i+a][3*j+b]
                else:
                    temp.append(data[3*i+a][3*j+b])
        info[name]=temp
val=1
for key in sorted(info):
    temp=(sorted(info[key]))
    print("#{}.".format(val),key)
    val2=1
    for a in temp:
        print("#{}-{}.".format(val,val2),a)
        val2+=1
    val+=1