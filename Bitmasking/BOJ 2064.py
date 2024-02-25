import sys
input = sys.stdin.readline
def printIP(ip):
    a = int(ip[:8], 2)
    b = int(ip[8:16], 2)
    c = int(ip[16:24], 2)
    d = int(ip[24:32], 2)
    print(str(a) +'.'+str(b) +'.'+ str(c) +'.' +str(d))

n = int(input())
address = []
for _ in range(n):
    a, b, c, d = map(int, input().split('.'))
    address.append(format(a,'08b')+format(b,'08b')+format(c,'08b')+bin(d,'08b'))

m = 0
for ip in address:
    for i in range(32):
        if address[0][i] != ip[i]:
            m = max(m, 32-i)

if m==0:
    network=address[0][:]
else:
    network = address[0][:-m] + '0'*m 
mask = '1'*(32-m) + '0'*m

printIP(network)
printIP(mask)