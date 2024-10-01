import sys
input = sys.stdin.readline

t, n = map(int, input().split())
location = [1] * (n + 1)
farmed = [[0] * 54 for _ in range(n + 1)]
bugs = []
bans = set()

for _ in range(t):
    num, player, action, *va = input().strip().split()
    player = int(player)
    
    if action == "M":
        new_location = int(va[0])
        location[player] = new_location
        
    elif action == "F":
        item_location = int(va[0])
        if location[player] == item_location:
            farmed[player][item_location] += 1
        else:
            bugs.append(int(num))
            farmed[player][item_location] += 1
    
    elif action == "C":
        item1, item2 = map(int, va)
        if farmed[player][item1] > 0 and farmed[player][item2] > 0:
            farmed[player][item1] -= 1
            farmed[player][item2] -= 1
        else:
            bugs.append(int(num))
            farmed[player][item1] = max(farmed[player][item1] - 1, 0)
            farmed[player][item2] = max(farmed[player][item2] - 1, 0)
    
    elif action == "A":
        target_player = int(va[0])
        if location[player] != location[target_player]:
            bugs.append(int(num))
            bans.add(player)

print(len(bugs))
if bugs:
    print(*sorted(bugs))

print(len(bans))
if bans:
    print(*sorted(bans))
