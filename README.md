# Housing_Portal

This repository contains a minimal example of a housing portal using Flask.
Users can register, log in, and submit a payment through Stripe Checkout.

## Requirements

- Python 3.8+
- Install dependencies using `pip install -r requirements.txt`.
- Set the environment variables `STRIPE_SECRET_KEY` and `STRIPE_PUBLISHABLE_KEY` with your Stripe credentials.
- Optionally set `FLASK_SECRET_KEY` to configure the session secret.

## Running

```
python app.py
```

Navigate to `http://localhost:5000` in your browser to test the payment flow.
