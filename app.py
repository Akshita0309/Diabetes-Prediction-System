import os
import uuid
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session
import matplotlib.pyplot as plt
import joblib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management
model = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
                'BMI', 'DiabetesPedigreeFunction', 'Age']

    input_data = [float(request.form[f]) for f in features]
    input_dict = dict(zip(features, input_data))

    # Predict
    prediction = model.predict([input_data])[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"

    # Categorize component status
    component_status = {}
    thresholds = {
        'Glucose': (70, 140),
        'BloodPressure': (80,120),
        'SkinThickness': (10, 50),
        'Insulin': (16, 166),
        'BMI': (18.5, 26.9),
        'DiabetesPedigreeFunction': (0.3, 1.0),
        'Pregnancies': (0, 3)
    }

    for key, val in input_dict.items():
        low, high = thresholds.get(key, (0, 100))
        if val < low:
            component_status[key] = 'Low'
        elif val > high:
            component_status[key] = 'High'
        else:
            component_status[key] = 'Normal'

    # Create graph
    if not os.path.exists('static/graphs'):
        os.makedirs('static/graphs')

    filename = str(uuid.uuid4()) + '.png'
    graph_path = os.path.join('static/graphs', filename)

    colors = ['red' if component_status[k] == 'High' else 'green' if component_status[k] == 'Low' else 'orange' for k in input_dict]
    plt.figure(figsize=(10, 4))
    plt.bar(input_dict.keys(), input_dict.values(), color=colors)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()

    # Store data in session
    session['result'] = result
    session['component_status'] = component_status
    session['input_dict'] = input_dict
    session['graph_image'] = filename

    return redirect(url_for('report'))

@app.route('/report')
def report():
    return render_template(
        'report.html',
        prediction_text=f"Prediction: {session.get('result', 'N/A')}",
        component_status=session.get('component_status', {}),
        input_dict=session.get('input_dict', {}),
        graph_image=session.get('graph_image', None)
    )

if __name__ == "__main__":
    app.run(debug=True)
