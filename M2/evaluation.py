import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd





QRELS_FILE = "q2/qrels2.txt"
QUERY_URL = "http://localhost:8983/solr/imdb_movies/select?fl=movie_title%2Coriginal_title%2Cyear%2Cgenre%2Cdirector%2Cactors%2Cdescription%2Ctomatometer_rating%2Creviews&indent=true&q.op=OR&q=actors%3A%20%22brad%20pitt%22%2C%20%22angelina%20jolie%22%5E10%0Amovie_title%5E2%0Aoriginal_title%5E2&rows=100"


# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance
results = requests.get(QUERY_URL).json()['response']['docs']


metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)


# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)



@metric
def ap(results, relevant):
    
    
    """Average Precision"""
    precision_values = [
        len([
            doc
            for doc in results[:idx]
            if doc['movie_title'] in relevant
        ]) / idx 
        for idx in range(1, len(results)+1)
    ]    
    
    if len(precision_values) == 0:
        return 0.0
    
    return sum(precision_values)/len(precision_values)


@metric
def p10(results, relevant, n=2):
    """Precision at N"""
    return len([doc for doc in results[:n] if doc['movie_title'] in relevant])/n


@metric
def r(results, relevant):
    return len([doc for doc in results if doc['movie_title'] in relevant])/len(relevant)


def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)


# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p10': 'Precision at 10 (P@10)',
    'r': 'Recall'
}


# Calculate all metrics and export results as LaTeX table
df = pd.DataFrame([['Metric','Value']] +
    [
        [evaluation_metrics[m], calculate_metric(m, results, relevant)]
        for m in evaluation_metrics
    ]
)


with open('q2/results2-boosted.tex','w') as tf:
    tf.write(df.to_latex())



# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([
        doc 
        for doc in results[:idx]
        if doc['movie_title'] in relevant
    ]) / idx 
    for idx, _ in enumerate(results, start=1)
]


recall_values = [
    len([
        doc for doc in results[:idx]
        if doc['movie_title'] in relevant
    ]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]


precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}


# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
recall_values = sorted(set(recall_values))

# Extend matching dict to include these new intermediate steps
for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if recall_values[idx-1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
        else:
            precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]


disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
disp.plot()

plt.ylim((0, 1.1))
plt.savefig('q2/precision_recall2-boosted.pdf')


