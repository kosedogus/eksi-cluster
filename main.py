import asyncio
import pandas as pd
import numpy as np
import openai

from scrape import get_topic
from translate import translate
from embedder import embedderEksi
from sklearn.cluster import KMeans



async def main():
    
    df = await get_topic('php',1,5)
    df['translation'] = df['entry']
    for i in range(len(df)):
        df.iloc[i, 1] = translate(df.iloc[i,0])
    print(df)
    df = embedderEksi(df)
    matrix = np.vstack(df.embedding.values)
    matrix.shape
    
    # clustering
    
    n_clusters = 2

    kmeans = KMeans(n_clusters=n_clusters, init="k-means++", random_state=42)
    kmeans.fit(matrix)
    labels = kmeans.labels_
    df["Cluster"] = labels
    
    print(df['Cluster'])

    
    return df

asyncio.run(main())