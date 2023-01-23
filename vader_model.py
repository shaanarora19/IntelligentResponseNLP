# -- REQUIRED LIBRARIES: --
# VADER: for Python 3+
# pip install vaderSentiment

# imports
import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class VaderModel:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def predict_sentiment(self, text: str):
        """
        Predict sentiment of a text using VADER
        :param text: text to predict sentiment for
        :return: sentiment score in a dictionary, formatted as follows:
        {
            'neg': negative sentiment score,
            'neu': neutral sentiment score,
            'pos': positive sentiment score,
            'compound': compound sentiment score
        }
        Where compound is the sum of all scores, normalized to be between -1 and 1.
        """
        return self.sia.polarity_scores(text)

    def add_scores_to_dataframe(self, df: pd.DataFrame, text_column: str):
        """
        Add sentiment scores to a dataframe
        :param df: dataframe to add scores to
        :param text_column: column in dataframe containing text to predict sentiment for
        :return: dataframe with sentiment scores added
        """

        # Make a temporary copy of the dataframe that will contain the new columns
        sentiment_df = df.copy()

        # Predict sentiment for each row in the dataframe
        sentiment_df['scores'] = sentiment_df[text_column].apply(lambda review: self.predict_sentiment(review))

        # Split the scores into their own columns
        sentiment_df['neg'] = sentiment_df['scores'].apply(lambda score_dict: score_dict['neg'])
        sentiment_df['neu'] = sentiment_df['scores'].apply(lambda score_dict: score_dict['neu'])
        sentiment_df['pos'] = sentiment_df['scores'].apply(lambda score_dict: score_dict['pos'])
        sentiment_df['compound']  = sentiment_df['scores'].apply(lambda score_dict: score_dict['compound'])

        return sentiment_df