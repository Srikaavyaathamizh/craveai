import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
import pickle
import pandas as pd
import pickle
from collections import Counter


def train_taste_predictor():
    df = pd.read_csv("data/user_history.csv")

    # Create a synthetic 'query' column
    df["query"] = (df["food_name"].astype(str) + " " +
                   df["location"].astype(str) + " " +
                   df["taste"].astype(str)).str.lower()

    X = df["query"]
    y = df["taste"]

    vectorizer = CountVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_vec, y)

    with open("ai/taste_model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)
# ai/predictor.py


def predict_tastes(user_id):
    try:
        with open("ai/taste_model.pkl", "rb") as f:
            vectorizer, model = pickle.load(f)

        df = pd.read_csv("data/user_history.csv")
        user_df = df[df["user_id"] == user_id]

        if user_df.empty:
            return []

        # Combine user query
        queries = (user_df["food_name"].astype(str) + " " +
                   user_df["location"].astype(str) + " " +
                   user_df["taste"].astype(str)).str.lower()

        X_vec = vectorizer.transform(queries)
        predictions = model.predict(X_vec)

        # Return top N most frequent predicted tastes
        top = Counter(predictions).most_common(3)
        return [taste for taste, _ in top]

    except Exception as e:
        print("Prediction error:", e)
        return []
