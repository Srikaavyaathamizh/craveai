import csv

def load_stalls_from_csv():
    stalls = []
    with open('data/stalls.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tastes = [t.strip() for t in (row.get("tastes") or "").split(';') if t.strip()]

            try:
                views = int((row.get("views") or "0").strip())
            except:
                views = 0

            try:
                rating = float((row.get("rating") or "0").strip())
            except:
                rating = 0.0

            stalls.append({
                "name": (row.get("name") or "").strip(),
                "food_type": (row.get("food_type") or "").strip(),
                "tastes": tastes,
                "image_url": (row.get("image_url") or "").strip(),
                "location": (row.get("location_name") or "").strip(),
                "views": views,
                "rating": rating,
                "owner_name": (row.get("owner_name") or "").strip()
            })
    return stalls
