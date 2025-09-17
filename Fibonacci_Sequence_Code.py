import matplotlib.pyplot as plt
n = 1000

fibonacci = [0,1]  # starting values

for i in range(2, n):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])


print("First 20 Fibonacci Sequence :" fibonacci[:20])

