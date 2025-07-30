from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

movies = pd.DataFrame({
    'title': ['Movie A', 'Movie B', 'Movie C'],
    'features': [[1, 0], [0, 1], [1, 1]]
})

cos_sim = cosine_similarity(movies['features'].tolist())
print("Similarity Matrix:\n", cos_sim)
