from flask import Blueprint, render_template, request, redirect, url_for, session

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def landing():
    return render_template('landing.html')

@user_bp.route('/user/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('data/sarab_ai.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('user.taste_preference'))
        else:
            return "Invalid user credentials!"

    return render_template('user_login.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def user_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('data/sarab_ai.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
        except sqlite3.IntegrityError:
            return "User already exists!"
        finally:
            conn.close()

        return redirect(url_for('user.user_login'))
    
    return render_template('user_register.html')


@user_bp.route('/taste_preference')
def taste_preference():
    return render_template('taste_preference.html')
