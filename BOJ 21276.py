import sys
input = sys.stdin.readline
n = int(input().strip())
data = input().split()
people = {}
for i, p in enumerate(data):
    people[p] = i+1

m = int(input().strip())

parents = [[] for _ in range(n+1)]
relation_set = set()
for _ in range(m):
    x, y = input().split()
    parents[people[x]].append(people[y])
    relation_set.add((people[x], people[y]))

immediate_parent = [0]*(n+1)
for i in range(1, n+1):
    if not parents[i]:
        immediate_parent[i] = 0 
    else:
        candidate = 0
        sorted_candidates = sorted(parents[i], key=lambda idx: data[idx-1])
        for cand in sorted_candidates:
            valid = True
            for other in parents[i]:
                if other == cand:
                    continue
                if (other, cand) in relation_set:
                    valid = False
                    break
            if valid:
                candidate = cand
                break
        immediate_parent[i] = candidate

children = [[] for _ in range(n+1)]
for i in range(1, n+1):
    p = immediate_parent[i]
    if p:
        children[p].append(i)

roots = []
for i in range(1, n+1):
    if immediate_parent[i] == 0:
        roots.append(data[i-1])
roots.sort()

print(len(roots))
print(" ".join(roots))
for name in sorted(data):
    idx = people[name]
    child_names = sorted([data[c-1] for c in children[idx]])
    if child_names:
        print(name, len(child_names), " ".join(child_names))
    else:
        print(name, 0)
