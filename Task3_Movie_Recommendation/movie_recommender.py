import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Improved dataset with descriptions
data = {
    "title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Titanic",
        "The Notebook",
        "Avengers: Endgame",
        "Iron Man",
        "The Conjuring",
        "Insidious",
        "The Hangover"
    ],
    "description": [
        "A thief enters dreams to steal secrets using advanced technology",
        "A team travels through space and a wormhole to save humanity",
        "Batman fights crime and chaos in Gotham City",
        "A romantic story set during the tragic sinking of a ship",
        "A heartfelt romantic love story between two young lovers",
        "Superheroes unite to defeat a powerful villain and save the universe",
        "A billionaire builds a high-tech armored suit to fight evil",
        "A family experiences terrifying paranormal events in their home",
        "A family is haunted by dark supernatural forces",
        "Three friends wake up after a wild night in Las Vegas"
    ],
    "genre": [
        "Sci-Fi Thriller",
        "Sci-Fi Drama",
        "Action Crime",
        "Romance Drama",
        "Romance",
        "Action Superhero",
        "Action Superhero",
        "Horror",
        "Horror Thriller",
        "Comedy"
    ]
}

df = pd.DataFrame(data)

# Combine genre + description
df["content"] = df["description"] + " " + df["description"] + " " + df["genre"]

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1,2))
genre_matrix = vectorizer.fit_transform(df["content"])

# Similarity calculation
similarity = cosine_similarity(genre_matrix)

def recommend(movie_title):
    if movie_title not in df["title"].values:
        print("Movie not found!")
        return
    
    index = df[df["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nMovies similar to {movie_title}:\n")

    for i in scores[1:6]:
        print(df.iloc[i[0]]["title"])

movie_name = input("Enter a movie name: ")
recommend(movie_name)