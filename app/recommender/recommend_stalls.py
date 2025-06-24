from geopy.distance import geodesic

def recommend_stalls(query, stalls):
    query = query.lower()
    results = []

    for stall in stalls:
        match_score = 0
        if query in stall["name"].lower():
            match_score += 2
        if query in stall["food_type"].lower():
            match_score += 1
        if query in stall["location"].lower():
            match_score += 1
        if query in stall["tastes"]:
            match_score += 2

        if match_score > 0:
            stall["match_score"] = match_score * 20  # out of 100
            results.append(stall)

    return sorted(results, key=lambda x: x["match_score"], reverse=True)
