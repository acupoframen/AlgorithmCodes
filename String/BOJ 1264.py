while True:
    answer=0
    n=input()
    if n=='#':
        break
    for x in n:
        if x in ['a','e','i','o','u','A','E','I','O','U']:
            answer+=1
    print(answer)