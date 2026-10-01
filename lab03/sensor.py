p = float(input())
n = int(input())
s = []
for x in range(n):
    x = input()
    if x != 'error':
        s.append(float(x))
k = [x for x in s if x > p]
print(n)
print(n - len(s))
print(len(k))
print(f'{(max(s)):.1f}')
print(f'{((sum(s)) / len(s)):.1f}')