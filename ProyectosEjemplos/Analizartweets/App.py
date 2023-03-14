import tweepy
from textblob import TextBlob


def autenticar(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def buscar_tweets(api, query, max_tweets=10):
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets):
        tweets.append(tweet.text)
    return tweets


def analizar_sentimiento(tweets):
    polaridades = []
    subjetividades = []
    for tweet in tweets:
        texto = TextBlob(tweet)
        polaridades.append(texto.sentiment.polarity)
        subjetividades.append(texto.sentiment.subjectivity)
    polaridad_promedio = sum(polaridades) / len(polaridades)
    subjetividad_promedio = sum(subjetividades) / len(subjetividades)
    return polaridad_promedio, subjetividad_promedio


consumer_key = "TU_CONSUMER_KEY"
consumer_secret = "TU_CONSUMER_SECRET"
access_token = "TU_ACCESS_TOKEN"
access_token_secret = "TU_ACCESS_TOKEN_SECRET"

api = autenticar(consumer_key, consumer_secret, access_token, access_token_secret)
query = "Python"
max_tweets = 100

tweets = buscar_tweets(api, query, max_tweets)
polaridad, subjetividad = analizar_sentimiento(tweets)

print("Análisis de sentimiento para la búsqueda de tweets de '{}'".format(query))
print("Polaridad promedio: {:.2f}".format(polaridad))
print("Subjetividad promedio: {:.2f}".format(subjetividad))
