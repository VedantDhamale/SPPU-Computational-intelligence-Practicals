import numpy as np, random

d=np.array([
     [0,10,15,20],
     [10,0,35,25],
     [15,35,0,30],
     [20,25,30,0]
])
n = len(d)
p = np.ones((n,n))

def tour():
    t = [random.randint(0, n-1)]
    while len(t) < n:
        prob = p[t[-1]] / (d[t[-1]] + 1e-6)
        prob[t] = 0
        prob /= prob.sum()
        t.append(np.random.choice(n, p=prob))
    return t

def length(t):
    return sum(d[t[i]][t[(i+1)%n]] for i in range(n))

best, best_len = None, 1e9

for _ in range(100):
    for _ in range(5):
        t = tour()
        l = length(t)
        if l < best_len: best, best_len = t, l
        for i in range(n): p[t[i]][t[(i+1)%n]] += 1/l
    p *= 0.5

print("Best tour:", best)
print("Length:", round(best_len,2))
