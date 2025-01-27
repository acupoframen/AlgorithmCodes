n=int(input())
pat=input()
front, back = pat.split('*')
for _ in range(n):
    file=input()
    if len(file)<len(front)+len(back):
        print("NE")
        continue
    if file.startswith(front) and file.endswith(back):
        print("DA")
    else:
        print("NE")