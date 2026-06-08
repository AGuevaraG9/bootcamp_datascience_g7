from flask import Flask, request, render_template
import joblib
import pandas as pd

# Cargar el modelo y los scalers
model_loaded = joblib.load('./model/model.pkl')
scaler_x_loaded = joblib.load('./model/scaler_x.pkl')
scaler_y_loaded = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    predicted_charges = None
    if request.method == 'POST':
        input_data = pd.DataFrame({
            'smoker': [float(request.form['smoker'])],
            'age': [float(request.form['age'])],
            'bmi': [float(request.form['bmi'])]
        })
        
        # Escalar los datos de entrada
        input_data_scaled = scaler_x_loaded.transform(input_data)
    
        # Realizar la predicción
        predicted_charges_scaled = model_loaded.predict(input_data_scaled)
    
        # Revertir la escala de la predicción a los valores originales
        predicted_charges = scaler_y_loaded.inverse_transform(predicted_charges_scaled)

        # Convertir a número simple y redondear
        predicted_charges = round(float(predicted_charges[0][0]), 2)

    return render_template(
        'index.html',
        predicted_charges=predicted_charges,
        form_data=request.form
    )
if __name__ == "__main__":
    app.run(debug=True)