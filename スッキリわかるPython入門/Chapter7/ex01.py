import math
import random
total = 0
num_inside = 0
sim_pi = 0
for total in range(1000):
    x = random.random()
    y = random.random()
    L = pow(x**2 + y**2, 0.5)
    total += 1
    if L <= 1:
        num_inside += 1
    sim_pi = 4 * num_inside / total
print(sim_pi)
print(total)
