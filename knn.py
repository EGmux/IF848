#simple implementation of knn
# applied to college.csv from Intro to statical learning book
import math
import pandas as pd
import matplotlib as plot
import numpy as np

def distance(x0, x1, feats):
    """
    compute n-dimensional euclidian distance
    """
    sum = 0;
    for feat in feats:
        sum += sum([math.pow(x0feat - x1feat, 2) for (x0feat,x1feat) in zip(x0.loc[feat], x1.loc[feat])])
    return math.sqrt(sum)

def normalize(x0):
    """
    given a row normalize each column
    """

def sorter(distances):
    """
    compute quicksort
    """
    pass

def knn(dataset, classes, features,k ):
    """
    given a dataset, set of classes, set of features/attributes and index collumn classify each row
    """
    df = pd.read_csv(dataset, usecols=features + classes)
    rows = []
    classifications = []
    for index, row in df.iterrows():
        rows.append(row)
    for row in rows:
        distances = [(point,distance(row, point,features)) for point in rows]
        sorted_distances = sorter(distances)[:k]
        probability = []
        for c in classes:
            probability.append(sum([1/k if classify(row[0]) == c else 0 for row in sorted_distances]))
        classifications.append(probability.index(max(probability)))









