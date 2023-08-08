Data Preprocessing:
Clean and preprocess the collected tweet data by removing duplicates, irrelevant content, and performing text preprocessing tasks like tokenization and removing stopwords.

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_tweet(tweet_text):
    # Remove special characters, URLs, and mentions
    cleaned_text = re.sub(r'http\S+', '', tweet_text)
    cleaned_text = re.sub(r'@\w+', '', cleaned_text)
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text)
    
    # Tokenize and remove stopwords
    words = word_tokenize(cleaned_text)
    words = [word.lower() for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    cleaned_words = [word for word in words if word not in stop_words]
    
    return ' '.join(cleaned_words)
