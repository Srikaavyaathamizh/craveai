from flask import Blueprint, render_template, request, redirect, url_for
import requests
from ai.scoring import compute_stall_score  # AI scoring logic
from ai.predictor import predict_tastes     # ML taste predictor
from rapidfuzz import fuzz
import csv

main_bp = Blueprint('main', __name__)

# ----------------------
# Route: Homepage
# ----------------------
@main_bp.route('/')
def index():
     return render_template('landing.html')


# ----------------------
# Route: Taste Preference Page
# ----------------------
@main_bp.route('/taste')
def taste_preference():
    return render_template('taste_preference.html')


# ----------------------
# Route: POST Taste + Location → Get Recommendations (Optional Flow)
# ----------------------
@main_bp.route('/get_recommendations', methods=['GET', 'POST'])
def get_recommendations():
    if request.method == 'GET':
        return redirect(url_for('main.taste_preference'))

    tastes = request.form.getlist('tastes')
    lat = float(request.form.get('lat', 0))
    lng = float(request.form.get('lng', 0))

    data = {
        "tastes": tastes,
        "location": [lat, lng]
    }

    try:
        res = requests.post("http://127.0.0.1:5000/recommend", json=data)
        stalls = res.json().get("recommendations", [])
    except Exception as e:
        print("Recommendation API error:", e)
        stalls = []

    return render_template("index.html", stalls=stalls)


# ----------------------
# Route: Main Page with Search + AI Scoring + Fuzzy Search
# ----------------------
@main_bp.route('/main')
def main_page():
    query = request.args.get('q', '').lower()
    user_id = int(request.args.get('user_id', 1))  # Simulated user_id

    # Use user query if exists, otherwise use predicted tastes
    user_preferences = query.split() if query else predict_tastes(user_id)
    query = query or ' '.join(user_preferences)  # Show predicted in search bar

    stalls = load_stalls_from_csv()

    for stall in stalls:
        combined_text = " ".join([
            stall["name"].lower(),
            stall["food_type"].lower(),
            " ".join(stall["tastes"]),
            stall["location_name"].lower()
        ])

        fuzzy_score = fuzz.partial_ratio(query, combined_text) if query else 0
        ai_score = compute_stall_score(stall, user_preferences)

        stall["score"] = ai_score + (fuzzy_score / 100.0)

    # Sort stalls by total score
    stalls = sorted(stalls, key=lambda x: x["score"], reverse=True)

    return render_template('main.html', stalls=stalls, query=query)


# ----------------------
# Helper: Load CSV Stall Data
# ----------------------
def load_stalls_from_csv():
    stalls = []
    with open('data/stalls.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tastes = [t.strip() for t in row.get("tastes", "").split(';') if t.strip()]

            try:
                views = int(row.get("views", "").strip())
            except:
                views = 0

            try:
                rating = float(row.get("rating", "").strip())
            except:
                rating = 0.0

            stall = {
                "name": row.get("name", ""),
                "food_type": row.get("food_type", ""),
                "tastes": tastes,
                "image_url": row.get("image_url", ""),
                "location_name": row.get("location_name", ""),
                "views": views,
                "rating": rating
            }
            stalls.append(stall)
    return stalls
