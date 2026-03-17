import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended = recommended[:k]
    hits = sum(1 for item in recommended if item in relevant)
    precision = hits/k
    recall = hits/len(relevant)
    return [precision, recall]
        