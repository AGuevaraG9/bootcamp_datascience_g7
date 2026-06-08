import joblib
import pandas as pd

# Cargar el modelo y los scalers
model_loaded = joblib.load('./model/model.pkl')
scaler_x_loaded = joblib.load('./model/scaler_x.pkl')
scaler_y_loaded = joblib.load('./model/scaler_y.pkl')

print('Modelo y scalers cargados exitosamente.')

# Preparar nuevos datos de entrada para la predicción
# El modelo fue entrenado con 'smoker', 'age', 'bmi'
# 'smoker': 1 para 'yes' (fumador), 0 para 'no' (no fumador)

def predict_charges(data):
    # Crear un DataFrame con los datos de entrada
    input_data = pd.DataFrame({
        'smoker': [data['smoker']],
        'age': [data['age']],
        'bmi': [data['bmi']]
    })
    
    # Escalar los datos de entrada
    input_data_scaled = scaler_x_loaded.transform(input_data)
    
    # Realizar la predicción
    predicted_charges_scaled = model_loaded.predict(input_data_scaled)
    
    # Revertir la escala de la predicción a los valores originales
    predicted_charges = scaler_y_loaded.inverse_transform(predicted_charges_scaled)
    
    return predicted_charges[0][0]

data = {
    'smoker': [1.0],  # Ejemplo: fumador
    'age': [36.0],    # Ejemplo: 36 años
    'bmi': [25.0]     # Ejemplo: BMI de 25
}

print(f"\nDatos de entrada para la predicción:\n{data}")

predicted_charges = predict_charges(data)

print(f"\nLa predicción de los cargos es: {predicted_charges:,.2f}")