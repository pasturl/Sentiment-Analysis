import pandas as pd

def convert_sentiment(x):
    if x == 2:
        return -1
    elif x == 4:
        return 1
    else:
        return x


def convert_sentiment_dublin(x):
    if x == "neutral":
        return -1
    elif x == "negative":
        return 0
    else:
        return 1
        

def read_dublin_data(filename):
    data = []
    df = pd.read_csv(filename, encoding="latin-1" )
    df['sentiment'] = df['sentiment'].apply(convert_sentiment_dublin)
    df = df[df['sentiment'] != -1].reset_index(drop=True)
    return df

  
def read_sentiment_data(filename):
    data = []
    col_names = ['sentiment', 'id', 'date', 'query', 'user', 'text']
    df = pd.read_csv(filename, encoding="latin-1", header = None, names = col_names)
    df['sentiment'] = df['sentiment'].apply(convert_sentiment)
    df = df[df['sentiment'] != -1]
    return df


def preprocess_data(df, stopwords):
    df['text_clean'] = df['text'].str.lower().apply(lambda x: [item for item in x.split() if item not in stopwords])
    df['text_clean'] = df['text_clean'].apply(lambda x: " ".join(x))
    return df