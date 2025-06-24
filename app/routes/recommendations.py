from flask import Blueprint, request, jsonify, render_template
from app.recommender.recommend_stalls import recommend_stalls
from app.recommender.load_data import load_stalls_from_csv


recommendations_bp = Blueprint('recommendations', __name__)

# Load stalls from CSV once at startup
stalls = load_stalls_from_csv()
@recommendations_bp.route('/main', methods=['GET'])
def main_page():
    query = request.args.get("q", "").strip().lower()

    filtered_stalls = []
    for stall in stalls:
        name = stall["name"].lower()
        food_type = stall["food_type"].lower()
        location = stall["location_name"].lower()
        tastes = [t.lower() for t in stall["tastes"]]

        match_score = 0
        if query:
            if query in name or query in food_type or query in location or query in tastes:
                match_score += 1

        if match_score > 0:
            stall_copy = stall.copy()
            stall_copy["match_score"] = match_score * 10
            filtered_stalls.append(stall_copy)

    return render_template("main.html", stalls=filtered_stalls, query=query)