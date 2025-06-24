answer=0
for i in range(3):
    n=input()
    if n.isnumeric():
        answer=int(n)+(3-i)

if answer%3==0:
    if answer%5:
        print("Fizz")
    else:
        print("FizzBuzz")
else:
    if answer%5:
        
        print(answer)
    else:
        
        print("Buzz")