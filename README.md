# How to Troll the World
## Analyzing the Russian troll tweets dataset through topic modeling, sentiment analysis, and word embeddings

In 2018, Twitter removed ~3,000 Russian-linked accounts and their 3 million tweets. Investigators have traced the accounts to a Kremlin-linked propaganda outfit founded in 2013 known as the Internet Research Agency (IRA). A team at NBC was able to reconstruct and publish a subset of 200,000 tweets from ~500 accounts - it's a fantastic story and I'd highly encourage [checking it out](https://www.nbcnews.com/tech/social-media/now-available-more-200-000-deleted-russian-troll-tweets-n844731). 

In the spirit of the 2020 US Presidential Election, I decided to dig into this dataset to explore the themes and sentiments of these tweets. 

You can [view the slides for my presentation at Metis here](https://github.com/scrapfishies/russian-troll-tweets-nlp/blob/main/presentation_slides.pdf).

---

## Methodologies and Workflow

I used natural language processing and unsupervised machine learning to tease out topics and sentiment, and used word embeddings and ScatterText to better understand word associations and tone within those topics. 

#### Workflow
1. Text preprocessing
  * Lowercase characters and remove punctuation, URLs, emojis, 
  * Remove stopwords - standard english, unique German words (there were quite a few German tweets in this dataset), and Twitter stopwords
  * Break up some key hashtags into separate words
  * Lemmatize words with SpaCy for topic modeling
2. Topic modeling discovery
  * Use LDA and pyLDAvis to simultaneously find top keywords for topics and interpret their relationships through interactive visualization
  * Use semi-supervised learning with CorEx topic-anchoring to dig deeper into topics and tease out sub-categories
3. Word embeddings visualizations
  * Train a gensim Word2Vec model
  * Use word vectors and word similarities to visualize and understand keyword relationships in core topics
4. Topics and sentiments trends over time
  * Plot LDA topics over time to understand trends
  * Use VADER sentiment analysis to quickly analyze tone of tweets and plot those trends by topic over time
5. ScatterText visualizations
  * Compare word frequencies between Clinton and Trump topics using ScatterText visualizations
  
## Key Findings, Implications, and Conclusions

I was able to extract the following topics from this corpus: 

* **Right wing news**: PJNET (Patriot Journalist Network), and other right wing outlets
* **Middle East**: terrorism and ISIS, anti-Islamic sentiments, refugee crises
* **Violence in the news**: lots of activity about BlackLivesMatter and police violence/brutality 
* **General Twitter chit-chat**: tweets about holidays, gaming, music, media, and other noise
* **Conservative chit-chat**: similar to General Twitter chit-chat, but with a more conservative/right-wing cultural lean
* **Hillary Clinton**: generally anti-Clinton tweets focused on her scandals (e.g. emails, Benghazi, health concerns)
* **Donald Trump**: generally pro-Trump campaign related tweets

Indeed there is some overlap or fluidity between topics. For example, much of Trump's campaign was focused on Hillary Clinton, so tweets in the Trump topic often contain references to her as well. 

Tracking topics over time is revealing. We can see that these accounts are relavtively quiet for a few years, and then a sudden flurry of activity around the 2016 election, with the Trump, Clinton, and the general/conservative chit-chat categories as the most prevelant. 

![Topics Time Series](https://github.com/scrapfishies/russian-troll-tweets-nlp/blob/main/img/top_freq_timeseries.png)

Unfortunately, trolling and the spread of misinformation and disinformation are not going away anytime soon. We can't rely on social media platforms to protect us - though *we can and **should*** continue to demand more from them. For now, healthy skepticism remains our best line of defense. 

As an online society, we need to continue to develop AI that can detect misinformation, disinformation, and deep fakes. We should also continue to analyze content from social media platforms, especially from the time surrounding the 2020 US Presidential Election, to continue to learn about troll behavior and build awareness. 

---

### Tools & Libraries
* Data Science essentials
  * Python
  * Jupyter Notebook
  * Pandas
  * NumPy

* Machine Learning
  * pyLDAvis
  * Latent Dirichlet Allocation (LDA)
  * Principal Component Analysis (PCA)

* Natural Language Processing
  * SpaCy
  * NLTK
  * sklearn
  * CorEx
  * VADER Sentiment Analysis
  * gensim (Word2Vec)
  * emoji
  
* Visualizations
  * Matplotlib
  * Seaborn
  * ScatterText
  * WordCloud
  * pyLDAvis

### Sources and References
- [NBC: Twitter deleted 200,000 Russian troll tweets. Read them here. (Ben Popken)](https://www.nbcnews.com/tech/social-media/now-available-more-200-000-deleted-russian-troll-tweets-n844731)
- [Kaggle: Russian Troll Tweets](https://www.kaggle.com/vikasg/russian-troll-tweets)
- [FiveThirtyEight: Russian Troll Tweets](https://github.com/fivethirtyeight/russian-troll-tweets)
