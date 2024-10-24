n=input()
answer=""
for i in range(len(n)):
    if n[i] not in "CAMBRIDGE":
        answer+=n[i]
print(answer)