n=int(input())
s=input()
if n<=25:
    print(s)
    exit(0)
if len(s[11:n-12].split('.'))<=1:
    print(s[:11]+'...'+s[n-11:])
else:
    print(s[:9]+'......'+s[n-10:])
