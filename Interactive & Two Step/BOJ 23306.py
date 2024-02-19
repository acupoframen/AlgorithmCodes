import sys
input=sys.stdin.readline
flush=sys.stdout.flush

n=int(input())
print("? 1")
flush()
first=int(input())
print("?",n)
flush()
end=int(input())
print("!",end-first)
flush()