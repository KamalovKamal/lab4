a = input()
list1 = list(map(int, a.split()))
b = input()
list2 = list(map(int, b.split()))
otvet = sorted(set(list1) & set(list2))
print(*(otvet))

