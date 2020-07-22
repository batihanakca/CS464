import csv
import math

prob_positive = 2004/11712
prob_negative = 7091/11712
prob_neutral = 2617/11712
alpha = 1
V = 5722
 
train= list()
labels= list()
test= list()
testlabels= list()

train_pos = list()
train_neg = list()
train_neut = list()

Y = [['positive'], ['negative'], ['neutral']]

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
  
total_word_occurance_pos = 0
total_word_occurance_neg = 0
total_word_occurance_neut = 0

for row in train_pos:
    for i in range(len(row)):
        total_word_occurance_pos = total_word_occurance_pos + int(row[i])
        
for row in train_neg:
    for i in range(len(row)):
        total_word_occurance_neg = total_word_occurance_neg + int(row[i])
    
for row in train_neut:
    for i in range(len(row)):
        total_word_occurance_neut = total_word_occurance_neut + int(row[i])
        
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
    occurance = occurance + 1
    
    return occurance

occurance_pos = list()
occurance_neg = list()
occurance_neut = list()

for i in range(5722):
    occurance_pos.append(word_occurance(i, "pos"))
    occurance_neg.append(word_occurance(i, "neg"))
    occurance_neut.append(word_occurance(i, "neut"))

def prediction(tweet):
    
    positive = math.log(prob_positive)
    negative = math.log(prob_negative)
    neutral = math.log(prob_neutral)

    for i in range(5722):
        if occurance_pos[i] > 0:
            positive = positive + (int(tweet[i]) * math.log(occurance_pos[i]/total_word_occurance_pos))       
    for i in range(5722):
        if occurance_neg[i] > 0:
            negative = negative + (int(tweet[i]) * math.log(occurance_neg[i]/total_word_occurance_neg))        
    for i in range(5722):
        if occurance_neut[i] > 0:
            neutral = neutral + (int(tweet[i]) * math.log(occurance_neut[i]/total_word_occurance_neut))
            
    if positive > negative:
        if positive > neutral:
            result = "positive"
    if negative > positive:
        if negative > neutral:
            result = "negative"
    if neutral >= positive:
        if neutral >= negative:
            result="neutral"
    
    return result

with open('question-4-test-features.csv', newline='') as csvfile:
    lines = csv.reader(csvfile)
    i=0
    for row in lines:
        test.append(row)
            
with open('question-4-test-labels.csv', newline='') as csvfile:
    lines = csv.reader(csvfile)
    i=0
    for row in lines:
        testlabels.append(row)

predicted = list()
true_pos = 0
true_neg = 0
true_neut = 0
false = 0

for i in range(len(test)):
    p = prediction(test[i])
    
    if p == testlabels[i][0]:
        if p == "positive":
            true_pos = true_pos + 1
        elif p == "negative":
            true_neg = true_neg + 1
        else:
            true_neut = true_neut + 1        
    else:
        false = false + 1
    true = true_pos + true_neg + true_neut    
    predicted.append(p)
    
print("True predictions: " + str(true))
print("Wrong predictions: " + str(false))
print("Accurracy: " + str(true*100/(true+false)) + "%")