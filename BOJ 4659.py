while True:
    n=input()
    if n=='end':
        break
    
    vowelapp=0
    vowels=0
    constant=0
    if n[0] in ['a','e','i','o','u']:
        vowels+=1
        vowelapp=1
    else:
        constant=1
    flag=1
    for i in range(1,len(n)):
        if n[i]==n[i-1]:
            if n[i] in ['e', 'o']:
                continue
            else:
                flag=0
                break
        if n[i] in ['a','e','i','o','u']:
            vowelapp=1
            vowels+=1
            constantt=0
            if vowels==3:
                flag=0
                break
        else:
            vowels=0
            constant+=1
            if constant==3:
                flag=0
                break
    if vowelapp and flag:
        print(f'<{n}> is acceptable.' )
    else:
        print(f'<{n}> is not acceptable.')