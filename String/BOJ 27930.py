data=list(input())
korea=list("KOREA")
yonsei=list("YONSEI")
for i in data:
    if i==korea[0]:
        del korea[0]
    if i==yonsei[0]:
        del yonsei[0]
    if not korea:
        print("KOREA")
        break
    if not yonsei:
        print("YONSEI")
        break