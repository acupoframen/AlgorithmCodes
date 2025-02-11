s = input()

s = s.replace("pi", " ")
s = s.replace("ka", " ")
s = s.replace("chu", " ")

if not s.strip():
    print("YES")
else:
    print("NO")