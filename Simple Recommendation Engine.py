from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# user-item matrix (rows: users, cols: items)
matrix = np.array([
    [5, 0, 3, 0],
    [4, 0, 0, 2],
    [0, 3, 4, 5]
])

# compute item-item similarity
sim = cosine_similarity(matrix.T)
print("Item-item similarity:\n", sim)
