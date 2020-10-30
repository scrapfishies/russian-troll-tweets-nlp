'''
Functions for preprocessing Tweets
'''

import re
import string


def remove_url(text):
    just_text = re.sub(r"http\S+", '', text, flags=re.MULTILINE)
    return just_text


def get_hashtags(text):
    hashtags = re.findall(r"\B#\w*[a-zA-Z]+\w*", text, flags=re.MULTILINE)
    clean_hashtags = [word.replace("#", "") for word in hashtags]
    return clean_hashtags


def remove_hashtags(text):
    clean_text = re.sub(r"\B#\w*[a-zA-Z]+\w*", "", text, flags=re.MULTILINE)
    return clean_text


def remove_rt_prefix(text):
    clean_text = re.sub(r"RT @\w*[a-zA-Z]+\w*:", "", text, flags=re.MULTILINE)
    return clean_text


def make_alphanumeric(text):
    clean_text = re.sub(r"\w*\d\w*", " ", text)
    return clean_text


def remove_punc(text):
    clean_text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
    return clean_text


def demojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def clean_tweet(tweet):
    cleaned_tweet = demojify(remove_punc(
        make_alphanumeric(remove_rt_prefix(remove_url(tweet))))).lower()
    cleaned_tweet = re.sub(r" +", " ", cleaned_tweet).strip()
    return cleaned_tweet
