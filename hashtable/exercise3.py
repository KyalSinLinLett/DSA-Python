# poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in python and print every word and its count as show below.
# Think about the best data structure that you can use to solve this problem and
# figure out why you selected that specific data structure.

word_list = []
word_dict = {}

with open('./datasets/poem.txt', 'r') as f:
    for row in f:
        tokens_per_row = row.split(' ')
        for token in tokens_per_row:
            word_list.append(token.replace('\n', ''))

for word in word_list:
    count = 0
    for match in word_list:
        if word == match:
            count += 1

    word_dict[word] = count


# print(word_list)
print(word_dict)
