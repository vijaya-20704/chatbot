import random
import json
import pickle 
import numpy as np 
import nltk
from nltk.stem import WordLemmatizier
from tensorflow.keras.models import Sequential
from tensor flow.keras.layers import Dense,Activation,Dropout
from tensorflow.keras.optimizers import SGD
lemmatizer=WordNetLemmatizer
intents=json.loads(open('intents.json').read())
words=[]
classes=[]
documents=[]
ignore_letters=['?','!','.',',']
for intent in intents['intents']:
  for pattern in intents['pattern']:
    word_list=nltk.word_tokenize(pattern)
    words.append(word_list)
    documents.append((words_list,intent['tag'])
    if intent['tag'] not in classes:
      classes.append(intent['tag'])
print(documents)
