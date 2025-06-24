# ----------------------
# Scoring Function (if not importing)
# ----------------------
def compute_stall_score(stall, user_preferences):
    score = 0

    name = stall.get("name", "").lower()
    food_type = stall.get("food_type", "").lower()
    tastes = [taste.lower() for taste in stall.get("tastes", [])]
    location_name = stall.get("location_name", "").lower()

    for pref in user_preferences:
        pref = pref.lower().strip()
        if pref in name:
            score += 5
        if pref in food_type:
            score += 3
        if any(pref in taste for taste in tastes):
            score += 2
        if pref in location_name:
            score += 2

    try:
        score += float(stall.get("rating", 0)) * 2
    except:
        pass

    try:
        score += int(stall.get("views", 0)) * 0.01
    except:
        pass

    return score
