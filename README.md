# CraveAI
# Crave.AI – AI-Based Food Stall Recommendation System

##  Aim
To develop an AI-powered web application that recommends food stalls based on user preferences like taste, food type, and location using natural language search, fuzzy logic, and machine learning.

---

##  Project Summary

crave.AI is a personalized street food recommendation platform. It allows:
- Users to discover stalls based on **taste**, **location**, or **stall name**.
- Owners to **register**, **login**, and **add stall details**.
- AI to recommend stalls using fuzzy matching and taste prediction via ML.

---

##  Features

-  Natural language & fuzzy search
-  Location and taste-based recommendation
-  Separate interfaces for **User** and **Owner**
-  Owner Dashboard with CSV storage
-  AI-powered taste prediction (KNN)
-  SQLite for login credential management

---

##  Technologies Used

- **Frontend**: HTML, CSS (Jinja templates)
- **Backend**: Flask (Python)
- **Database**: SQLite (for user/owner login)
- **Data Storage**: CSV (for stalls), Pickle (ML model)
- **AI**: 
  - Fuzzy Search (custom logic)
  - Taste prediction using **KNeighborsClassifier**
- **Libraries**: `sklearn`, `pandas`, `geopy`, `flask`, `csv`, `pickle`

---

##  System Workflow

1. **User Registration/Login**
2. **Taste Preference Selection**
3. **Search stalls** using taste, food, or location
4. **ML predicts user's likely tastes** (if history exists)
5. **Stalls ranked** using NLP/fuzzy relevance
6. **Owners login/register**
7. **Owners add stall info** stored in CSV
8. **Owner Dashboard** displays only their stalls

---
## How AI Works in Sarab.AI
 **Fuzzy/NLP-Based Search (in recommend_stalls)**

    Uses string similarity to match query with:

        stall name

        food type

        taste

        location

 **Taste Prediction (in predictor.py)**

    KNN model trained on user food history

    Predicts top 3 likely tastes for a given user

## Result:
Crave.AI successfully recommends food stalls based on user taste and location preferences using AI techniques like fuzzy search and taste prediction, providing personalized and relevant stall suggestions.
