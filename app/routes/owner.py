from flask import Blueprint, render_template, request, redirect, url_for,session
import csv,sqlite3
from app.recommender.load_data import load_stalls_from_csv


owner_bp = Blueprint('owner', __name__, url_prefix='/owner')

STALLS_CSV = 'data/stalls.csv'
@owner_bp.route('/login', methods=['GET', 'POST'])
def owner_login():
    if request.method == 'POST':
        ownername = request.form['username']  
        password = request.form['password']

        conn = sqlite3.connect('data/sarab_ai.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM owners WHERE ownername=? AND password=?", (ownername, password))
        owner = cursor.fetchone()
        conn.close()

        if owner:
            session['owner_name'] = ownername
            return redirect(url_for('owner.add_stall'))  # 🔄 Redirect to form page
        else:
            return "Invalid owner credentials!"

    return render_template('owner_login.html')



@owner_bp.route('/register', methods=['GET', 'POST'])
def owner_register():
    if request.method == 'POST':
        ownername = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('data/sarab_ai.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO owners (ownername, password) VALUES (?, ?)", (ownername, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Owner already exists!"
        finally:
            conn.close()

        return redirect(url_for('owner.owner_login'))
    
    return render_template('owner_register.html')

@owner_bp.route('/add_stall', methods=['GET', 'POST'])
def add_stall():
    if request.method == 'POST':
        new_entry = {
            'name': request.form['name'],
            'food_type': request.form['food_type'],
            'tastes': request.form['tastes'],
            'image_url': request.form['image_url'],
            'location': request.form['location'],
            'owner_name': session.get('owner_name', 'Unknown')
        }

        fieldnames = ['name', 'food_type', 'tastes', 'image_url', 'location', 'owner_name']

        with open('data/stalls.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:  # File is empty → write headers
                writer.writeheader()
            writer.writerow(new_entry)

        return redirect(url_for('owner.owner_dashboard'))

    return render_template('stall_form.html')

from flask import session, render_template
from app.recommender.load_data import load_stalls_from_csv

@owner_bp.route('/dashboard')
def owner_dashboard():
    owner_name = session.get('owner_name')
    all_stalls = load_stalls_from_csv()
    
    # Only keep stalls for current owner
    owner_stalls = [stall for stall in all_stalls if stall.get("owner_name") == owner_name]

    return render_template('owner_dashboard.html', stalls=owner_stalls)




