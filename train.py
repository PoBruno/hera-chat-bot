import json
import pickle
import nltk
import random
import numpy as np

from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# inicializaremos nossa lista de palavras, classes, documentos e 
# definimos quais palavras serão ignoradas
words = []
documents = []
intents = json.loads(open('intents.json').read())
# adicionamos as tags em nossa lista de classes
classes = [i['tag'] for i in intents['intents']]
ignore_words = ["!", "@", "#", "$", "%", "*", "?"]

# é feita a leitura do arquivo intents.json e transformado em json
intents = json.loads(open('intents.json').read())

# percorremos nosso array de objetos
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # com ajuda no nltk fazemos aqui a tokenizaçao dos patterns 
        # e adicionamos na lista de palavras
        word = nltk.word_tokenize(pattern)
        words.extend(word)

        # adiciona aos documentos para identificarmos a tag para a mesma
        documents.append((word, intent['tag']))


