#text1 = 'meaningful_text1.txt'
#text2 = 'meaningful_text2.txt'
"""
text1 = 'random_letters.txt'
text2 = 'random_letters2.txt'


text1 = 'Alice_25000.txt'
text2 = 'os_25000.txt'
"""

correct = 0
"""
print(len(t1))
print(len(t2))

for i in range(len(t1) - 1):
    if t1[i] == t2[i]:
        correct += 1
"""

A_3000 = open('data/Alice_3000.txt')
A_10000 = open('data/Alice_10000.txt')
A_25000 = open('data/Alice_25000.txt')
o_3000 = open('data/os_3000.txt')
o_10000 = open('data/os_10000.txt')
o_25000 = open('data/os_25000.txt')

Alice_3000 = A_3000.read()
Alice_10000 = A_10000.read()
Alice_25000 = A_25000.read()
os_3000 = o_3000.read()
os_10000 = o_10000.read()
os_25000 = o_25000.read()


result = []
print('два осмысленных текста:')
for i in range(len(Alice_3000) - 1):
    if Alice_3000[i] == os_3000[i]:
        correct += 1
print('\tДлина 3000 символов:', correct/3000)
result.append(correct/3000)
correct = 0

for i in range(len(Alice_10000) - 1):
    if Alice_10000[i] == os_10000[i]:
        correct += 1
print('\tДлина 10000 символов:', correct/10000)
result.append(correct/10000)
correct = 0

for i in range(len(Alice_25000) - 1):
    if Alice_25000[i] == os_25000[i]:
        correct += 1
print('\tДлина 25000 символов:', correct/25000)
result.append(correct/25000)
correct = 0

o_3000.close()
o_10000.close()
o_25000.close()

l1_3000 = open('data/random_letters1_3000.txt')
l1_10000 = open('data/random_letters1_10000.txt')
l1_25000 = open('data/random_letters1_25000.txt')

letters1_3000 = l1_3000.read()
letters1_10000 = l1_10000.read()
letters1_25000 = l1_25000.read()

print('Осмысленный текст и текст из случайных букв:')
for i in range(len(Alice_3000) - 1):
    if Alice_3000[i] == letters1_3000[i]:
        correct += 1
print('\tДлина 3000 символов:', correct/3000)
result.append(correct/3000)
correct = 0

for i in range(len(Alice_10000) - 1):
    if Alice_10000[i] == letters1_10000[i]:
        correct += 1
print('\tДлина 10000 символов:', correct/10000)
result.append(correct/3000)
correct = 0

for i in range(len(Alice_25000) - 1):
    if Alice_25000[i] == letters1_25000[i]:
        correct += 1
print('\tДлина 25000 символов:', correct/25000)
result.append(correct/3000)
correct = 0

w1_3000 = open('data/random_words1_3000.txt')
w1_10000 = open('data/random_words1_10000.txt')
w1_25000 = open('data/random_words1_25000.txt')

word1_3000 = w1_3000.read()
word1_10000 = w1_10000.read()
word1_25000 = w1_25000.read()

print('Осмысленный текст и текст из случайных слов:')
for i in range(len(Alice_3000) - 1):
    if Alice_3000[i] == word1_3000[i]:
        correct += 1
print('\tДлина 3000 символов:', correct/3000)
result.append(correct/3000)
correct = 0

for i in range(len(Alice_10000) - 1):
    if Alice_10000[i] == word1_10000[i]:
        correct += 1
print('\tДлина 10000 символов:', correct/10000)
result.append(correct/3000)
correct = 0

for i in range(len(Alice_25000) - 1):
    if Alice_25000[i] == word1_25000[i]:
        correct += 1
print('\tДлина 25000 символов:', correct/25000)
result.append(correct/3000)
correct = 0

A_3000.close()
A_10000.close()
A_25000.close()

l2_3000 = open('data/random_letters2_3000.txt')
l2_10000 = open('data/random_letters2_10000.txt')
l2_25000 = open('data/random_letters2_25000.txt')
letters2_3000 = l2_3000.read()
letters2_10000 = l2_10000.read()
letters2_25000 = l2_25000.read()

print('Два текста из случайных букв:')
for i in range(len(letters1_3000) - 1):
    if letters2_3000[i] == letters1_3000[i]:
        correct += 1
print('\tДлина 3000 символов:', correct/3000)
result.append(correct/3000)
correct = 0

for i in range(len(letters1_10000) - 1):
    if letters2_10000[i] == letters1_10000[i]:
        correct += 1
print('\tДлина 10000 символов:', correct/10000)
result.append(correct/3000)
correct = 0

for i in range(len(letters1_25000) - 1):
    if letters2_25000[i] == letters1_25000[i]:
        correct += 1
print('\tДлина 25000 символов:', correct/25000)
result.append(correct/3000)
correct = 0

l1_3000.close()
l1_10000.close()
l1_25000.close()
l2_3000.close()
l2_10000.close()
l2_25000.close()
w2_3000 = open('data/random_letters2_3000.txt')
w2_10000 = open('data/random_letters2_10000.txt')
w2_25000 = open('data/random_letters2_25000.txt')
word2_3000 = w2_3000.read()
word2_10000 = w2_10000.read()
word2_25000 = w2_25000.read()

print('Два текста из случайных слов:')
for i in range(len(word1_3000) - 1):
    if word2_3000[i] == word1_3000[i]:
        correct += 1
print('\tДлина 3000 символов:', correct/3000)
result.append(correct/3000)
correct = 0

for i in range(len(word1_10000) - 1):
    if word2_10000[i] == word1_10000[i]:
        correct += 1
print('\tДлина 10000 символов:', correct/10000)
result.append(correct/3000)
correct = 0

for i in range(len(word1_25000) - 1):
    if word2_25000[i] == word1_25000[i]:
        correct += 1
print('\tДлина 25000 символов:', correct/25000)
result.append(correct/3000)
correct = 0
