chislo = int(input())
s = set(range(1,chislo+1))
x = s
while True:
    key = input()
    if (key == 'HELP'):
        print(*sorted(x))
        break
    key = {int(i) for i in key.split()}
    if (len(x & key) > len(x)/2):
        print('YES')
        x &= key
    else:
        print('NO')
        x &= s - key
