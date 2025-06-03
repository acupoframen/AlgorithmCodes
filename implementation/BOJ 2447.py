def draw_stars(n):
    if n==1:
        return ['*']

    stars=draw_stars(n//3)
    data=[]

    for star in stars:
        data.append(star*3)
    for star in stars:
        data.append(star+' '*(n//3)+star)
    for star in stars:
        data.append(star*3)
    return data

N=int(input())
print('\n'.join(draw_stars(N)))