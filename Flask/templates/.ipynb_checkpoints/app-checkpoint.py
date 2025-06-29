from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model and encoders
model = pickle.load(open('model.pkl', 'rb'))
encoder = pickle.load(open('encoder.pkl', 'rb'))  # LabelEncoder for 'holiday' and 'weather'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form input
        temp = float(request.form['temp'])
        rain = float(request.form['rain'])
        snow = float(request.form['snow'])
        holiday = request.form['holiday']
        weather = request.form['weather']
        day = int(request.form['day'])
        month = int(request.form['month'])
        year = int(request.form['year'])
        hours = int(request.form['hours'])
        minutes = int(request.form['minutes'])
        seconds = int(request.form['seconds'])

        # Encode categorical features
        holiday_encoded = encoder.transform([holiday])[0]
        weather_encoded = encoder.transform([weather])[0]

        # Create feature vector
        features = np.array([[holiday_encoded, temp, rain, snow, weather_encoded, day, month, year, hours, minutes, seconds]])

        # Predict
        prediction = model.predict(features)[0]
        return render_template('index.html', prediction_text=f'Predicted Traffic Volume: {int(prediction)}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if _name_ == '_main_':
    app.run(debug=True)