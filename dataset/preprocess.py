import os
from random import shuffle

ALL = 'all.txt'
TRAIN = 'train.txt'
VAL = 'val.txt'

# <path-to-wav-file>|<text-corresponding-to-speech-in-wav>|<speaker-no>|<lang-no>

lines = []
speakers = set()
langs = set()
with open(ALL, 'r',encoding='utf-8') as f:
    for line in f:
        # print(line)
        id, s, l, p, t = line.split('\n')[0].split('|')
        p = 'dataset/clean_comvoi/' + p
        s = l+s
        lines.append((p, t, s, l))
        speakers.add(s)
        langs.add(l)

speakers = list(speakers)
print('Total speakers: ', len(speakers))
langs = list(langs)
print('Total languages: ', len(langs))
newlines = []
for p, t, s, l in lines:
    s = speakers.index(s)
    l = langs.index(l)
    newlines.append(f'{p}|{t}|{s}|{l}')

shuffle(newlines)
k = int(0.9 * len(newlines))
train = newlines[:k]
val = newlines[k:]
print('Total train files: ', len(train))
print('Total val files: ', len(val))


with open(TRAIN, 'w',encoding='utf-8') as f:
    for line in train:
        f.write(line + '\n')

with open(VAL, 'w',encoding='utf-8') as f:
    for line in val:
        f.write(line + '\n')