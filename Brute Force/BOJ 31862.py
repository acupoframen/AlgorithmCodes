from itertools import product
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
score = [0] * (n + 1)
notfinished = []

for _ in range(m):
    a, b, c = map(int, input().split())
    if c == 0:
        notfinished.append((a, b))  
    elif c == 1:
        score[a] += 1  
    else:
        score[b] += 1  

notfinishedlen = len(notfinished)

answer = 0

def dfs(depth, curr_score, max_score, max_count):
    global answer
    
    if depth == notfinishedlen:
        if curr_score[k] == max_score and max_count == 1:
            answer += 1
        return

    a, b = notfinished[depth]

    curr_score[a] += 1
    if curr_score[a] > max_score:
        dfs(depth + 1, curr_score, curr_score[a], 1)
    elif curr_score[a] == max_score:
        dfs(depth + 1, curr_score, max_score, max_count + 1)
    else:
        dfs(depth + 1, curr_score, max_score, max_count)
    curr_score[a] -= 1 

    curr_score[b] += 1
    if curr_score[b] > max_score:
        dfs(depth + 1, curr_score, curr_score[b], 1)
    elif curr_score[b] == max_score:
        dfs(depth + 1, curr_score, max_score, max_count + 1)
    else:
        dfs(depth + 1, curr_score, max_score, max_count)
    curr_score[b] -= 1  
    
initial_max_score = max(score)
initial_max_count = score.count(initial_max_score)
dfs(0, score, initial_max_score, initial_max_count)

print(answer)
