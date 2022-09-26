n = int(input())
fibonacci = [1, 1]

for x in range(n+1):
    fibonacci.append(fibonacci[-2]+fibonacci[-1])
print(fibonacci)