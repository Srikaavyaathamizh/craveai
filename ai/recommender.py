from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

def recommend_stalls(user_tastes, user_location, stalls):
    recommendations = []

    for stall in stalls:
        taste_match = len(set(user_tastes) & set(stall['tastes']))
        distance = haversine(user_location[1], user_location[0], stall['location'][1], stall['location'][0])
        score = taste_match - (distance / 10)  # Prefer taste match, penalize distance

        recommendations.append({
            "name": stall["name"],
            "location": stall["location"],
            "tastes": stall["tastes"],
            "score": round(score, 2),
            "distance_km": round(distance, 2)
        })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return recommendations