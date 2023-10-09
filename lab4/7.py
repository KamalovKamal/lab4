n = int(input())  
possible_numbers = set(range(1, n + 1)) 

while True:
    question = input()
    if question == "HELP":
        break
    
    numbers = set(map(int, question.split())) 
    answer = input()  
    if answer == "YES":
        possible_numbers.intersection_update(numbers)
    else:
        possible_numbers.difference_update(numbers)
result = sorted(possible_numbers)
print(" ".join(map(str, result)))
