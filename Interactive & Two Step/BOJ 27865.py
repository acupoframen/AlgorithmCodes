import sys
input=sys.stdin.readline
flush=sys.stdout.flush

n=int(input())
while True:
    print("? 1") 
    flush()
    n=input().strip()
    if n=="Y":
        print("! 1")
        flush()
        exit(0)