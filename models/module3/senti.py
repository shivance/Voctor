from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

clf = SentimentIntensityAnalyzer()


def sentiment(text):
    d = clf.polarity_scores(text)
    print(type(d))
    Keymax = max(d, key=lambda x: d[x])

    if Keymax == 'pos':
        return 1
    elif Keymax == 'neg':
        return -1
    else:
        return 0
