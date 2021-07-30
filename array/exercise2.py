heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

# 1. length of list
print(len(heros))

# 2. add 'black panther' at the end
heros.append('black panther')
print(heros)

# 3. bp after hulk
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

# 4. rm thor and hulk, replace with dr. strange
heros[1:3] = ['doctor strange']
print(heros)

# 5. sort heros alphabetically
print(sorted(heros))
