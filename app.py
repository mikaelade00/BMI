from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open('models/model_pipeSVM.pkl', 'rb'))  # Replace "your_model.pkl" with your model file name

@app.route('/')
def index():
    return render_template('Untitled-1.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data from the request
        gender = request.form['gender']
        #gender = 0 if gender == "Male" else 1
        height = float(request.form['height'])
        weight = float(request.form['weight'])

        # Perform prediction using the model
        prediction = model.predict([[height, weight]])

        # Map prediction class labels to GMI labels
        if prediction[0] == 0:
            gmi_label = "Extremely Weak"
        if prediction[0] == 1 :
            gmi_label ="Weak" 
        if prediction[0] == 2:
            gmi_label ="Normal" 
        if prediction[0] == 3:
            gmi_label ="Overweight"
        if prediction[0] == 4:
            gmi_label ="Obesity" 
        if prediction[0] == 5:
            gmi_label ="Extreme Obesity"

        return render_template('Untitled-1.html', prediction_result=f'Predicted BMI: {gmi_label}')
    except Exception as e:
        return render_template('Untitled-1.html', prediction_result=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run()
