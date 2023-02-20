data=input()
def recursion(str):
    if len(str)==1:
        return True
    elif len(str)==2:
        if str[0]==str[1]:
            return True
        else:
            return False
    temp=len(str)//2
    if str[:temp:]!=str[:len(str)-temp-1:-1]:
        return False
    if recursion(str[:temp:]) and recursion(str[:len(str)-temp-1:-1]):
        return True
    else:
        return False
if recursion(data):
    print("AKARAKA")
else:
    print("IPSELENTI")