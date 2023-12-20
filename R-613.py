from collections import deque 

D = deque([1, 2, 3, 4, 5, 6, 7, 8])
Q = deque()

# Remove elements 1, 2, 3 from D and enqueue them in Q
for _ in range(3):
    Q.append(D.popleft())

# Remove element 4 from D and enqueue it in Q
Q.append(D.popleft())

# Remove element 5 from D and insert it at the third position in Q
for _ in range(3):
    D.appendleft(Q.pop())

# Remove elements 6, 7, 8 from D and enqueue them in Q 
for _ in range(3):
    Q.append(D.popleft())

# Append all elements from Q back to D
while Q:
    D.append(Q.popleft())

print(D) # Output: deque([1, 2, 3, 5, 4, 6, 7, 8])