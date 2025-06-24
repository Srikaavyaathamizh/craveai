
# import json
# from ai.recommender import recommend_stalls

# # Load stall data from JSON
# with open("data/stalls.json", "r") as f:
#     stalls = json.load(f)

# # Convert location lists to tuples for calculation
# for stall in stalls:
#     stall["location"] = tuple(stall["location"])

# # Sample user input
# user_tastes = ["spicy"]
# user_location = (12.9719, 77.5937)

# # Get recommendations
# results = recommend_stalls(user_tastes, user_location, stalls)

# # Show results
# print("\n📍 Top Recommended Stalls:\n")
# for i, stall in enumerate(results, start=1):
#     print(f"{i}. {stall['name']} - Score: {stall['score']} - Distance: {stall['distance_km']} km - Tastes: {stall['tastes']}")
