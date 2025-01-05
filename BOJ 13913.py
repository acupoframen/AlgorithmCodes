from collections import deque

def find_shortest_path(n, k):
    MAX = 100000  
    visited = [-1] * (MAX + 1)  
    prev = [-1] * (MAX + 1)
    q = deque()
    q.append(n)
    visited[n] = 0  
    while q:
        curr = q.popleft()
        if curr == k:
            
            path = []
            while curr != -1:
                path.append(curr)
                curr = prev[curr]
            return visited[k], path[::-1] 

        for next_pos in (curr - 1, curr + 1, curr * 2):
            if 0 <= next_pos <= MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[curr] + 1  
                prev[next_pos] = curr  
                q.append(next_pos)

n, k = map(int, input().split())
time, path = find_shortest_path(n, k)
print(time)
print(*path)
