numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  

occurances = []
for index, num in enumerate(numbers):
    if num == number_to_find:
        occurances.append(index)
        
print(occurances)