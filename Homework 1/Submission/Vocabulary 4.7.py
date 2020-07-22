import csv

train= list()
labels= list()

train_pos = list()
train_neg = list()
train_neut = list()

Y = [['positive'], ['negative'], ['neutral']]

fileHandle = open('question-4-vocab.txt', encoding="utf8")
vocab = list()
for line in fileHandle:
    vocab.append(line)
fileHandle.close()

words = list()

for line in vocab:
    pos = line.index("\t")
    num = line[:pos]
    words.append(num)
    

with open('question-4-train-features.csv', newline='') as csvfile:
    lines = csv.reader(csvfile)
    i=0
    for row in lines:
        train.append(row)
    
with open('question-4-train-labels.csv', newline='') as csvfile:
    lines = csv.reader(csvfile)
    i=0
    for row in lines:
        labels.append(row)
        
i = 0
for row in train:
    if labels[i] == Y[0]:
        train_pos.append(row)
    elif labels[i] == Y[1]:
        train_neg.append(row)
    elif labels[i] == Y[2]:
        train_neut.append(row)
    i = i + 1
    
def word_occurance(i, label):
    occurance = 0
    
    if label == 'pos':
        for row in train_pos:
            occurance = occurance + int(row[i])
    elif label == 'neg':
        for row in train_neg:
            occurance = occurance + int(row[i])
    elif label == 'neut':
        for row in train_neut:
            occurance = occurance + int(row[i])  
    return occurance

occurance_pos = list()
occurance_neg = list()
occurance_neut = list()

for i in range(5722):
    occurance_pos.append(word_occurance(i, "pos"))
    occurance_neg.append(word_occurance(i, "neg"))
    occurance_neut.append(word_occurance(i, "neut"))

positive_20 = list()
negative_20 = list()
neutral_20 = list()

positive_20_words = list()
negative_20_words = list()
neutral_20_words = list()

print("Most Common 20 Words in Positive Tweets")
print("_______________________________________")
for i in range(20):
    index = occurance_pos.index(max(occurance_pos))
    occurance_pos[index] = 0
    positive_20.append(index)
    positive_20_words.append(words[index])
    print(words[index])
    
print()
print("Most Common 20 Words in Negative Tweets")
print("_______________________________________")
for i in range(20):
    index = occurance_neg.index(max(occurance_neg))
    occurance_neg[index] = 0
    negative_20.append(index)
    negative_20_words.append(words[index])
    print(words[index])
    
print()
print("Most Common 20 Words in Neutral Tweets")
print("_______________________________________")
for i in range(20):
    index = occurance_neut.index(max(occurance_neut))
    occurance_neut[index] = 0
    neutral_20.append(index)
    neutral_20_words.append(words[index])
    print(words[index])
