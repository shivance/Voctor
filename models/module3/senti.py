from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

clf = SentimentIntensityAnalyzer()


def sentiment(text):
    clf.polarity_scores(text)
