n = int(input())
all_l = set()
any_l = set()

for _ in range(n):
    num_l = int(input())
    student_l = set()
    
for _ in range(num_l):
        language = input()
        student_l.add(language)
if not all_l:
        all_l = student_l.copy()
        any_l = student_l.copy()
else:
         all_l.intersection_update(student_l)
        
         any_l.update(student_l)

print(len(all_l))
for language in sorted(all_l):
    print(language)

print(len(any_l))
for language in sorted(any_l):
    print(language)


