import sys

input = sys.stdin.readline
events = []
queries = []

while True:
    try:
        line = input().strip()
        parts = line.split()
        if parts[0] == 'Query':
            queries.append(int(parts[1]))
        elif parts[0] == 'Chocolate':
            events.append((int(parts[1]), 'Chocolate', float(parts[2])))
        elif parts[0] == 'Coffee':
            events.append((int(parts[1]), 'Coffee', float(parts[2])))
    except IndexError:
        break
queries.sort()

def safety_distance(query_time):
    total = 0.0
    for t, kind, n in events:
        if query_time < t:
            continue
        dt = query_time - t
        if kind == 'Chocolate':
            effect = 8 * n - dt / 12.0
        else:  
            effect = 2 * n - (dt * dt) / 79.0
        if effect > 0:
            total += effect
    return max(1.0, total)

for T in queries:
    dist = safety_distance(T)
    print(f"{T} {round(dist, 1)}")
