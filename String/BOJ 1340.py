date=input().split()
totalminute=365*24*60
days={
    "January"   : 31,
    "February"  : 28,
    "March"     : 31,
    "April"     : 30,
    "May"       : 31,
    "June"      : 30,
    "July"      : 31,
    "August"    : 31,
    "September" : 30,
    "October"   : 31,
    "November"  : 30,
    "December"  : 31,
}
if not int(date[2])%400 or (not int(date[2])%4 and int(date[2])%100):
    days["February"]+=1
    totalminute+=24*60

day=0
for mon,d in days.items():
    if mon==date[0]:
        break
    else:
        day+=d

hour=int(date[3][0:2])
minute=int(date[3][3:])
days=int(date[1][0:-1])-1

answer=(day+days)*24*60+60*hour+minute
print(answer/totalminute*100)