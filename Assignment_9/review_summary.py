import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function to read reviews from a .txt file
def read_reviews(file_path):
    with open(file_path, 'r') as file:
        reviews = file.read()
    return reviews

# Function to create a concise third-person summary
def summarize_reviews(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    
    # Filter out punctuation and stopwords
    filtered_words = [word for word in words if word not in stop_words and word not in string.punctuation]
    
    # Calculate word frequency
    word_freq = defaultdict(int)
    for word in filtered_words:
        word_freq[word] += 1

    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Score sentences based on word frequency
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] += word_freq[word]
    
    # Select sentences while ensuring key points are included
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    
    # Prepare to create a more concise summary
    summary = []
    unique_points = set()

    # Construct the summary with key points, avoiding repetition
    for sentence in summarized_sentences:
        if len(summary) < 5:  # Limit to 5 key sentences
            summary.append(sentence.strip())
            unique_points.update(word_tokenize(sentence.lower()))

    # Prepare a cohesive third-person style summary
    summary_text = ' '.join(summary)
    
    # Ensure proper punctuation and spacing
    summary_text = summary_text.replace(" .", ".").replace(" ,", ",").replace(" !", "!").replace(" ?", "?")
    summary_text = summary_text[0].upper() + summary_text[1:]  # Capitalize first letter

    # Modify the summary to make it sound like a third person is summarizing
    summary_text = summary_text.replace(" I ", " users ").replace(" my ", " their ").replace(" me ", " them ")
    summary_text = summary_text.replace(" users'm ", " users're ").replace(" users'v ", " users've ")

    # Additional logic to make the text sound more cohesive
    summary_text = "Overall, users find that " + summary_text + "."

    return summary_text

# File paths
positive_reviews_file = 'positive_reviews.txt'
negative_reviews_file = 'negative_reviews.txt'
neutral_reviews_file = 'neutral_reviews.txt'

# Read reviews
positive_reviews = read_reviews(positive_reviews_file)
negative_reviews = read_reviews(negative_reviews_file)
neutral_reviews = read_reviews(neutral_reviews_file)

# Summarize reviews with third-person narrative
positive_summary = summarize_reviews(positive_reviews)
negative_summary = summarize_reviews(negative_reviews)
neutral_summary = summarize_reviews(neutral_reviews)

# Display summaries in the terminal
print("==== Positive Reviews Summary ====")
print(positive_summary)

print("\n==== Negative Reviews Summary ====")
print(negative_summary)

print("\n==== Neutral Reviews Summary ====")
print(neutral_summary)

# Optionally, save summaries to files
with open('positive_summary.txt', 'w') as pos_file:
    pos_file.write(positive_summary)

with open('negative_summary.txt', 'w') as neg_file:
    neg_file.write(negative_summary)

with open('neutral_summary.txt', 'w') as neu_file:
    neu_file.write(neutral_summary)

print("\nSummaries in third person have been saved to text files!")
