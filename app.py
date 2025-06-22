import os
from flask import Flask, render_template, redirect, url_for, request
import stripe

app = Flask(__name__)

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "sk_test_placeholder")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pay', methods=['GET', 'POST'])
def pay():
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
