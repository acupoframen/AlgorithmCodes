from collections import defaultdict
dic=defaultdict(list)
while True:
    try:
        word=input()
        dic["".join(sorted(word))].append(word)
    except:
        break
sorteddic={k:[sorted(set(v)),len(dic[k])] for k,v in dic.items()}
sorteddic=sorted(sorteddic.items(),key=lambda x:(-x[1][1],sorted(x[1][0])[0]))

for i in range(5):
    print("Group of size %s: %s ." %(sorteddic[i][1][1]," ".join(sorteddic[i][1][0])))