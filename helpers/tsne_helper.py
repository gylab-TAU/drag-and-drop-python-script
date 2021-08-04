from sklearn.manifold import TSNE
import pandas as pd
from helpers import helper

def get_fashion_tsne(df):
    data = []
    for i in range(1, len(df)):
        line = []
        for j in range(1, len(df[1])):
            line.append(df[i][j])
        data.append(line)
    df = pd.DataFrame(data, columns=df[0][1:])

    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    labels_dic = {}  # label is picture name
    for i in range(df.shape[0]):
        labels_dic[i] = df.columns[i]
    df = df.rename(labels_dic, axis='index')
    df = df.rename(labels_dic, axis='columns')

    RS = 1
    tsne_object = TSNE(method="exact", metric="precomputed", random_state=RS,
                       perplexity=5)
    fashion_tsne = tsne_object.fit_transform(df)

    return fashion_tsne

def get_tsne(df):
    fashion_tsne = get_fashion_tsne(df)

    fields = ["identity", "x", "y"]
    res = []

    for i in range(len(fashion_tsne)):
        line = []

        id = labels_dic[i].split("_")[0]
        x = fashion_tsne[i][0]
        y = fashion_tsne[i][1]

        line.append(id)
        line.append(x)
        line.append(y)

        res.append(line)

    return pd.DataFrame(res, columns=fields)