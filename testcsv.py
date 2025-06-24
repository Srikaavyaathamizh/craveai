import csv

def load_stalls_from_csv(file_path='data/stalls.csv'):
    stalls = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                stalls.append({
                    "name": row.get("name", ""),
                    "food_type": row.get("food_type", ""),
                    "location_name": row.get("location_name", ""),
                    "tastes": [t.strip() for t in row.get("tastes", "").split(",")],
                    "image_url": row.get("image_url", "")
                })
    except Exception as e:
        print("Error loading CSV:", e)
    return stalls

if __name__ == '__main__':
    stalls = load_stalls_from_csv()
    print(f"Loaded {len(stalls)} stalls")
    for stall in stalls:
        print(stall)
