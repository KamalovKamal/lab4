lines = int(input())
words = set()

for _ in range(lines):
    line = input()
    words1 = line.split()  
    words.update(words1)

print(len(words))
