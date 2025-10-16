import pandas as pd
import re
import collections
import matplotlib.pyplot as plt

d = collections.Counter()


def get_player_usernames():
    df = pd.read_csv('manutd_player_accounts.csv')
    return set(df['accounts'].apply(lambda x: x.split('/')[-1].lower()))


def count_username(usernames):
    df = pd.read_csv('manutd_tweets.csv')
    df['text'].apply(lambda x: search_words(x, usernames))


def search_words(text, usernames):
    global d
    result = re.findall(r'\b@\w+', text)
    if result:
        for res in result:
            temp = res.lower()[1:]
            if temp in usernames:
                d[temp] += 1


def plot_mentions():
    global d
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    bars = plt.bar(*zip(*d.items()))
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.1, yval + .005, yval)
    plt.xticks(rotation=45)
    plt.show()


count_username(usernames=get_player_usernames())
plot_mentions()
