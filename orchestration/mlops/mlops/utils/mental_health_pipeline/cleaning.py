import pandas as pd
import re

import nltk
import re

# Download the stopwords resource
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

stemmer = nltk.SnowballStemmer("english")

def removal(text):
    text = str(text).lower()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [w for w in text.split(' ') if w not in stopwords]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text