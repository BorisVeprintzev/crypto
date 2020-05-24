import csv
import pandas as pd
import random
import string
#Alice1 = open('Alice_10000.txt', 'w')
#Alice2 = open('Alice.txt' , 'r')

file_path = 'english-word-frequency/unigram_freq.csv'
english_words = []
f1 = open('data/random_words1.txt', 'w')
f2 = open('data/random_words2.txt', 'w')

reader = pd.read_csv(file_path)
a = reader['word'][:500]
for i in range(500):
    english_words.append(a[i])

for w in range(10000):
    f1.write(random.choice(english_words) + ' ')
    f2.write(random.choice(english_words) + ' ')

f1.close()
f2.close()
f1 = open('data/random_words1.txt', 'r')
f2 = open('data/random_words2.txt', 'r')
f_n1 = open('data/random_words1_10000.txt', 'w')
f_n2 = open('data/random_words2_10000.txt', 'w')
f_n3 = open('data/random_words1_25000.txt', 'w')
f_n4 = open('data/random_words2_25000.txt', 'w')
f_n5 = open('data/random_words1_3000.txt', 'w')
f_n6 = open('data/random_words2_3000.txt', 'w')
tmp1 = f1.read()
tmp2 = f2.read()
f_n1.write(tmp1[:10000])
f_n2.write(tmp2[:10000])
f_n3.write(tmp1[:25000])
f_n4.write(tmp2[:25000])
f_n5.write(tmp1[:3000])
f_n6.write(tmp2[:3000])
#Alice1.write(a1[:25000])
#Alice1.write(a1[:10000])

t_n1 = open('data/Alice_10000.txt', 'w')
t_n2 = open('data/Alice_25000.txt', 'w')
t_n3 = open('data/Alice_3000.txt', 'w')
t_n4 = open('data/os_10000.txt', 'w')
t_n5 = open('data/os_25000.txt', 'w')
t_n6 = open('data/os_3000.txt', 'w')
t1 = open('data/Alice.txt' , 'r')
t2 = open('data/os.txt', 'r')
a = t1.read()
b = t2.read()

t_n1.write(a[:10000])
t_n2.write(a[:25000])
t_n3.write(a[:3000])
t_n4.write(b[:10000])
t_n5.write(b[:25000])
t_n6.write(b[:3000])

text1 = open('data/random_letters1_25000.txt', 'w')
text2 = open('data/random_letters2_25000.txt', 'w')
t3 = open('data/random_letters1_10000.txt', 'w')
t4 = open('data/random_letters2_10000.txt', 'w')
t5 = open('data/random_letters1_3000.txt', 'w')
t6 = open('data/random_letters2_3000.txt', 'w')

for i in range(25000):
    text1.write(random.choice(string.ascii_letters))
    text2.write(random.choice(string.ascii_letters))

for i in range(10000):
    t3.write(random.choice(string.ascii_letters))
    t4.write(random.choice(string.ascii_letters))

for i in range(3000):
    t5.write(random.choice(string.ascii_letters))
    t6.write(random.choice(string.ascii_letters))