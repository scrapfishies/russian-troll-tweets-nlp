'''
Functions for preprocessing Tweets
'''

import emoji
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


### Dealing with Emojis ###

def get_emojis(text):
    emoji_list = [char for char in text if char in emoji.UNICODE_EMOJI]
    return emoji_list


def emoji_as_words(emoji_list):
    emoji_literal = [emoji.demojize(em, delimiters=('', ''))
                     for em in emoji_list]
    return emoji_literal


def emojize(emoji_literal_list):
    emojified = [emoji.emojize(':' + em + ':') for em in emoji_literal_list]
    return emojified


def demojify(text):
    regrex_pattern = re.compile(pattern="["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                "]+", flags=re.UNICODE)
    clean_text = regrex_pattern.sub(r'', text)
    return clean_text


### Compiled cleaning function ###

def clean_tweet(tweet):
    cleaned_tweet = demojify(remove_punc(
        make_alphanumeric(remove_rt_prefix(remove_url(tweet))))).lower()
    cleaned_tweet = re.sub(r" +", " ", cleaned_tweet).strip()
    cleaned_tweet = re.sub(r"([^\x00-\x7F])+", " ", cleaned_tweet)
    return cleaned_tweet


######### HASHTAG DICT #########

hashtag_dict = {'realdonaldtrump': 'real donald trump',
                'hillaryclinton': 'hillary clinton',
                'neverhillary': 'never hillary',
                'trumpforpresident': 'trump for president',
                'islamkills': 'islam kills',
                'hrc': 'hillary clinton',
                'stopislam': 'stop islam',
                'icelebratetrumpwith': 'i celebrate trump with',
                'reasonstoprotest': 'reasons to protest',
                'trumpsfavoriteheadline': 'trumps favorite headline',
                'merkelmussbleiben': 'merkel muss bleiben',
                'tedcruz': 'ted cruz',
                'draintheswamp': 'drain the swamp',
                'potuslasttweet': 'potus last tweet',
                'giftideasforpoliticians': 'gift ideas for politicians',
                'thingspeopleontwitterlike': 'things people on twitter like',
                'trumpbecause': 'trump because',
                'nocybercensorship': 'no cyber censorship',
                'votetrump': 'vote trump',
                'demdebate': 'dem debate',
                'gopdebate': 'gop debate',
                'rednationrising': 'red nation rising',
                'hillarysemails': 'hillarys emails',
#                 'clintonoriginalbirther': 'clinton original birther',
#                 'trumptrain': 'trump train',
#                 'oscarhasnocolor': 'oscar has no color',
#                 'basketofdeplorables': 'basket of deplorables',
                'billclinton': 'bill clinton',
                'imwithher': 'im with her',
                'nowplaying': 'now playing',
#                 'opiceisis': 'op ice isis',
#                 'iceisis': 'ice isis',
#                 'tcot': 'top conservatives on twitter',
#                 'ccot': 'christian conservatives on twitter',
                'donaldtrump': 'donald trump',
                'newhampshire': 'new hampshire',
                'trumppence': 'trump pence',
                'trumpwinsbecause': 'trump wins because',
                'djt': 'donald j trump',
#                 'hillaryrottenclinton': 'hillary rotten clinton',
#                 'whereshillary': 'wheres hillary',
#                 'dncleak': 'dnc leak',
                'johnpodesta': 'john podesta',
                'trum': 'trump',
                'melaniatrump': 'melania trump',
                'hillarysemail': 'hillarysemails',
                'trumpp': 'trump'
                }
