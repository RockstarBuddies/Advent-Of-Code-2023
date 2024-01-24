plan = list(map(str.split, open('input18.txt')))
dirs = {'R': (1,0), 'D': (0,1), 'L': (-1,0), 'U': (0,-1),'0': (1,0), '1': (0,1), '2': (-1,0), '3': (0,-1)}
def f(steps, pos=0, ans=1):
    for (x,y), n in steps:
        pos += x*n
        ans += y*n * pos + n/2
    return int(ans)
print(f((dirs[d],    int(s))          for d,s,_ in plan), f((dirs[c[7]], int(c[2:7], 16)) for _,_,c in plan))
