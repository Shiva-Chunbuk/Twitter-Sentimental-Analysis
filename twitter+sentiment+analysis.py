# -*- coding: utf-8 -*-
"""twitter+sentiment+analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11Wr367Z6nO7qtqoUt1sly3X8HPPXvFnr?usp=sharing
"""

#Import the libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read the data
df=pd.read_csv('sentiment.csv')

#Check first 5 rows
df.head()

#size of data
df.shape

#Total no. of classes in target value
df['label'].value_counts()

#Seems like a class imbalance problem.

#Understanding the sentiments in the data
df[df['label']==0].head(10)

df[df['label']==1].head(10)

#Lets classify the tweets into positive or negative sentiment.

df.isnull().sum()

#ID is not helpful so remove it.
df.drop(['id'],axis=1,inplace=True)
df.head()

#Data preprocessing

import string
string.punctuation

#function to remove punctuation

def clean(text):
    remv_pun=[char for char in text.lower() if char not in string.punctuation]
    remv_punc_join = ''.join(remv_pun)
    return remv_punc_join

clean(' @ Great beginning,,, takes! time,,,.   #run')

tweets_df_clean = df['tweet'].apply(clean)

tweets_df_clean[6]

tweets_df_clean.head()

#Install a popular nlp library called nltk
!pip install nltk

import nltk

# Download the stopwords resource
nltk.download('stopwords')

# Import the stopwords and print the first 5
from nltk.corpus import stopwords
stopwords_list = stopwords.words('english')
print(stopwords_list[:5])

tweets_df = pd.DataFrame(tweets_df_clean)
tweets_df.columns

# stopwords treatment and converting the data into lower case
def stop(text):
    remv_stop = [a for a in text.split() if a.lower() not in stopwords]
    remv_stop_join = ' '.join(remv_stop)
    return remv_stop_join

import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Load your DataFrame containing tweets (replace this with your actual code)
# tweets_df = ...

# Load the English stopwords list
stopwords_list = stopwords.words('english')

# Function to remove stopwords and convert text to lowercase
def remove_stopwords_and_lowercase(text):
    words = text.split()  # Split the text into words
    filtered_words = [word for word in words if word.lower() not in stopwords_list]
    processed_text = ' '.join(filtered_words)
    return processed_text

# Example usage
tweet = tweets_df['tweet'][0]  # Replace 0 with the index of the tweet you want to process
processed_tweet = remove_stopwords_and_lowercase(tweet)
print(processed_tweet)

# Define a list of stopwords
stopwords = ["the", "and", "in", "to", "of", "a", "for", "on", "with", "this"]

# Modify the stop function to use the list of stopwords
def stop(text):
    remv_stop = [word for word in text.split() if word.lower() not in stopwords]
    remv_stop_join = ' '.join(remv_stop)
    return remv_stop_join

# Apply the stop function to the 'tweet' column of the DataFrame
tweets_df['tweet'] = tweets_df['tweet'].apply(stop)

tweets_df_stopwords[:2]

tweets_df_stopwords = pd.DataFrame(tweets_df_stopwords)
tweets_df_stopwords

from nltk.stem import PorterStemmer
st = PorterStemmer()

def steming(text):
    ste = [st.stem(word) for word in text.split()]
    ste_join = ' '.join(ste)
    return ste_join

tweets_df_stem = tweets_df_stopwords['tweet'].apply(steming)

tweets_df_stem[:2]

# The dataset has been stemmed to its root word

tweets_df_stopwords['tweet'][0]

#Applying Lemmatization
from nltk.stem import WordNetLemmatizer

wl = WordNetLemmatizer()

import nltk
nltk.download('wordnet')

def lematize(text):
    ste = [wl.lemmatize(word) for word in text.split()]
    ste_join = ' '.join(ste)
    return ste_join

lematize('Dog keepss on barkings')

tweets_df_stopwords.iloc[:2]

tweets_df_stem = pd.DataFrame(tweets_df_stem)
tweets_df_stem.head()

# Applying the Count Vectorizer

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000)

sen = tweets_df_stem['tweet'].tolist()
len(sen)

from pandas import DataFrame

def document_matrix(text, vectorizer):
    mat = vectorizer.fit_transform(text)
    return DataFrame(mat.toarray())

m = document_matrix(sen,cv)
m.head()

from sklearn.feature_extraction.text import TfidfVectorizer


tfidf_vec = TfidfVectorizer(max_features=2500)

#Splitting the data into dependent and independent variable

y= df['label']
y.head()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(m,y,test_size=0.33,random_state=25)

x_train.shape
y_train.shape

from sklearn.naive_bayes import MultinomialNB
NaiveBclassifier = MultinomialNB()
NaiveBclassifier.fit(x_train,y_train)

# Predicting train cases
y_pred_train = NaiveBclassifier.predict(x_train)

from sklearn.metrics import accuracy_score
#Accuracy Score

acc = accuracy_score(y_train, y_pred_train)
acc
