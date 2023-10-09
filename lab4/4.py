number = input().split()
s = set()
for x in number:
    if x in s:
        print('YES')
    else:
        print('NO')
        s.add(x)