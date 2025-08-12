# Diabetes-Prediction-System
The Diabetes Prediction System is a web-based application designed to predict whether a person is likely to have diabetes based on key medical attributes. It leverages Machine Learning for predictive analysis and provides users with a detailed health report along with visual insights.

The system accepts inputs such as:
Number of pregnancies
Glucose level
Blood pressure
Skin thickness
Insulin level
Body Mass Index (BMI)
Diabetes pedigree function
Age

Using a trained ML model, the system classifies the patient as Diabetic or Not Diabetic and highlights which health indicators are outside the normal range. It also generates a color-coded bar graph to visually represent these values, helping users easily identify potential health risks.

Concepts & Methods Used

Machine Learning Concepts:
      Supervised Learning – The model is trained using labeled medical data.
      Classification – Binary classification to determine "Diabetic" or "Not Diabetic".
      Scikit-learn model training and prediction (model saved as diabetes_model.pkl).

Flask Web Framework:
      Routing – Handles different pages (/ for input, /predict for prediction, /report for results).
      Template Rendering – Dynamic HTML pages (index.html, report.html) for user interaction.
      Session Management – Stores prediction results and user input temporarily for report generation.

Data Visualization:
      Matplotlib – Creates bar graphs showing user input values with colors indicating health status:
      Red → High
      Green → Low
      Orange → Normal

Data Preprocessing & Thresholding
      Normal range thresholds defined for each parameter.
      Automatic categorization of each value into Low, Normal, or High.

Deployment & File Handling
      Joblib – Loads the pre-trained model.
      UUID – Generates unique filenames for graphs to avoid conflicts.
      Static Files – Stores generated graphs for display in reports.
