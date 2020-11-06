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
                'wakeupamerica': 'wake up america',
                'neverhillary': 'never hillary',
                'trumpforpresident': 'trump for president',
                'islamkills': 'islam kills',
                'blacklivesmatter': 'black lives matter',
                'survivalguidetothanksgiving': 'survival guide to thanksgiving',
                'christmasaftermath': 'christmas aftermath',
                'teaparty': 'tea party',
                'betteralternativetodebates': 'better alternative to debates',
                'crookedhillary': 'crooked hillary',
                'thingsmoretrustedthanhillary': 'things more trusted than hillary',
                'ruinadinnerinonephrase': 'ruin a dinner in one phrase',
                'makemehateyouinonephrase': 'make me hate you in one phrase',
                'idrunforpresidentif': 'id run for president if',
                'ihavearighttoknow': 'i have a right to know',
                'hrc': 'hillary clinton',
                'foxnews': 'fox news',
                'stopislam': 'stop islam',
                'icelebratetrumpwith': 'i celebrate trump with',
                'reasonstoprotest': 'reasons to protest',
                'trumpsfavoriteheadline': 'trumps favorite headline',
                'merkelmussbleiben': 'merkel muss bleiben',
                'rejecteddebatetopics': 'rejected debate topics',
                'makeamericagreatagain': 'make america great again',
                'todolistbeforechristmas': 'to',
                'debatenight': 'debate night',
                'cruzcrew': 'cruz crew',
                'tedcruz': 'ted cruz',
                'draintheswamp': 'drain the swamp',
                'potuslasttweet': 'potus last tweet',
                'giftideasforpoliticians': 'gift ideas for politicians',
                'hillaryshealth': 'hillarys health',
                'hillaryforprison': 'hillary for prison',
                'thingspeopleontwitterlike': 'things people on twitter like',
                'obamaswishlist': 'obamas wish list',
                'trumpbecause': 'trump because',
                'nocybercensorship': 'no cyber censorship',
                'votetrump': 'vote trump',
                'nevertrump': 'never trump',
                'americafirst': 'america first',
                'demdebate': 'dem debate',
                'gopdebate': 'gop debate',
                'rednationrising': 'red nation rising',
                'hillarysemails': 'hillarys emails',
                'clintonoriginalbirther': 'clinton orginal birther',
                'trumptrain': 'trump train',
                'oscarhasnocolor': 'oscar has no color',
                'clintonoriginalbirther': 'clinton original birther',
                'basketofdeplorables': 'basket of deplorables',
                'billclinton': 'bill clinton',
                'imwithher': 'im with her',
                'nowplaying': 'now playing',
                'opiceisis': 'op ice isis',
                'iceisis': 'ice isis',
                'tcot': 'top conservatives on twitter',
                'ccot': 'christian conservatives on twitter',
                'pjnet': 'patriot journalist network',
                'donaldtrump': 'donald trump',
                'newhampshire': 'new hampshire',
                'trumppence': 'trump pence',
                'trumpwinsbecause': 'trump wins because',
                'djt': 'donald j trump',
                'hillaryrottenclinton': 'hillary rotten clinton',
                'whereshillary': 'wheres hillary',
                'dncleak', 'dnc leak',
                'johnpodesta': 'john podesta'
                }
