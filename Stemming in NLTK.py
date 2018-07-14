from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps= PorterStemmer()

words=["python","pythoner","pythoning","pythoned"]

for w in words:
    print(ps.stem(w))

    
