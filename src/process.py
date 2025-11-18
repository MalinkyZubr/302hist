import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



EXCLUDED_CHARACTERS = " <>=@^]`[\_{}|*"
ALLOWED_CHARACTERS = "".join(chr(x) for x in range(32, 123) if chr(x) not in EXCLUDED_CHARACTERS)

print(ALLOWED_CHARACTERS)

nltk.download("all")


def preprocess_text(text: str) -> str:
    text = "".join([char for char in text if char in ALLOWED_CHARACTERS])
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]

    processed_text = ' '.join(lemmatized_tokens)

    return processed_text


def get_sentiment(preprocessed_text: str, analyzer: SentimentIntensityAnalyzer) -> dict:
    scores = analyzer.polarity_scores(preprocessed_text)

    return scores


if __name__ == "__main__":
    analyzer = SentimentIntensityAnalyzer()
    text = """

    """
    text = preprocess_text(text)
    print(get_sentiment(text, analyzer))