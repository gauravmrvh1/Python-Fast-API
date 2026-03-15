import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


print("\n")
df = pd.read_csv("netflix_data.csv")

# | Movie           | sci-fi | kids | fight | supernatural | monsters | crime | chemistry | teacher | drug | lord | group | bank | robbery | time | travel | mystery | comedy | friends |
# | --------------- | ------ | ---- | ----- | ------------ | -------- | ----- | --------- | ------- | ---- | ---- | ----- | ---- | ------- | ---- | ------ | ------- | ------ | ------- |
# | Stranger Things | 1      | 1    | 1     | 1            | 1        | 0     | 0         | 0       | 0    | 0    | 0     | 0    | 0       | 0    | 0      | 0       | 0      | 0       |
# | Breaking Bad    | 0      | 0    | 0     | 0            | 0        | 1     | 1         | 1       | 1    | 1    | 0     | 0    | 0       | 0    | 0      | 0       | 0      | 0       |
# | Money Heist     | 0      | 0    | 0     | 0            | 0        | 1     | 0         | 0       | 0    | 0    | 1     | 1    | 1       | 0    | 0      | 0       | 0      | 0       |
# | Dark            | 1      | 0    | 0     | 0            | 0        | 0     | 0         | 0       | 0    | 0    | 0     | 0    | 0       | 1    | 1      | 1       | 0      | 0       |
# | Friends         | 0      | 0    | 0     | 0            | 0        | 0     | 0         | 0       | 0    | 0    | 0     | 0    | 0       | 0    | 0      | 0       | 1      | 1       |

print(df + "\n")

print("\n")
df["combined_features"] = df["genre"] + " " + df["description"]
print(df + "\n")
print("\n")

vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(df["combined_features"])
similarity = cosine_similarity(feature_matrix)
print("\n ******************* similarity ******************* \n")
print(similarity)
print("\n ******************* feature_matrix ******************* \n")
print(feature_matrix)



def recommend_movie(movie_title):

    movie_index = df[df.title == movie_title].index[0]

    similar_movies = list(enumerate(similarity[movie_index]))

    sorted_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)[1:4]

    for movie in sorted_movies:
        print(df.iloc[movie[0]].title)

recommend_movie("Money Heist")