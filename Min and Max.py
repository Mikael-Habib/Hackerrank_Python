# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,m = map(int,input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
    arr = np.array(l)
print(np.max(np.min(arr, axis = 1)))
