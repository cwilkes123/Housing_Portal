import os
from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-me")

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "sk_test_placeholder")

# In-memory user store for demo purposes
users = {
    'admin': generate_password_hash('password')
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'User already exists', 400
        users[username] = generate_password_hash(password)
        session['user'] = username
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pw_hash = users.get(username)
        if pw_hash and check_password_hash(pw_hash, password):
            session['user'] = username
            return redirect(url_for('index'))
        return 'Invalid credentials', 401
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        try:
            stripe.Charge.create(
                amount=1000,
                currency='usd',
                description='Housing fee',
                source=request.form['stripeToken']
            )
            return redirect(url_for('success'))
        except stripe.error.StripeError:
            return 'Payment error', 400
    return render_template('pay.html', publishable_key=os.environ.get('STRIPE_PUBLISHABLE_KEY', 'pk_test_placeholder'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
