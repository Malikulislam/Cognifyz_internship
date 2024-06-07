import nltk
nltk.download('punkt')
nltk.download('stopwords')
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

def preprocess_text(text):
    # Clean and preprocess text reviews
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]  # Remove non-alphabetic tokens
    tokens = [token for token in tokens if token not in stopwords.words('english')]  # Remove stopwords
    return tokens

data['Cleaned Reviews'] = data['Rating text'].apply(preprocess_text)

# Identify common positive and negative keywords
positive_keywords = Counter()
negative_keywords = Counter()

for index, row in data.iterrows():
    if row['Rating text'] == 'Positive':
        positive_keywords.update(row['Cleaned Reviews'])
    elif row['Rating text'] == 'Negative':
        negative_keywords.update(row['Cleaned Reviews'])

# Calculate average review length
data['Review Length'] = data['Cleaned Reviews'].apply(len)
average_review_length = data['Review Length'].mean()

# Explore relationship between review Length and rating
plt.scatter(data['Review Length'], data['Aggregate rating'])
plt.xlabel('Review Length')
plt.ylabel('Aggregate Rating')
plt.title('Review Length vs. Aggregate Rating')
plt.show()

# Display results
print("Most Common Positive Keywords:", positive_keywords.most_common(10))
print("Most Common Negative Keywords:", negative_keywords.most_common(10))
print("Average Review Length:", average_review_length)