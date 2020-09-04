import re
import csv
import pickle
import time
import pprint
from collections import Counter
from datetime import datetime, timedelta
from urllib.request import urlopen

from bs4 import BeautifulSoup

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from textblob import TextBlob

import spacy
# only run line 21 if language model has not been pre-installed
# !python -m spacy download en_core_web_lg
spacy_nlp = spacy.load('en_core_web_md')
from spacy import displacy
from spacy.lang.en.stop_words import STOP_WORDS
spacy.prefer_gpu()

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tag.perceptron import PerceptronTagger
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

from dictionaries import lexicon, negate
# line 35 imports our proprietary sentiment algorithm
from sentiment_algos import proprietary_sentiment_normalised

from yellowbrick.text import FreqDistVisualizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import warnings
warnings.filterwarnings('ignore')