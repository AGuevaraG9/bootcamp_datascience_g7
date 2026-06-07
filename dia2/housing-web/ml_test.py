import joblib
import numpy as np
import sklearn

model = joblib.load('./model/model.pkl')
sc_x = joblib.load('./model/scaler_x.pkl')
sc_y = joblib.load('./model/scaler_y.pkl')

def predict_price(rooms):
    rooms_sc = sc_x.transform(np.array([[rooms]]))
    prediction_sc = model.predict(rooms_sc)
    prediction = sc_y.inverse_transform(prediction_sc) * 10000
    return prediction[0][0]

rooms = int(input("Ingrese el nro de habitaciones : "))
price = predict_price(rooms)
print(f'El precio de una casa con {rooms} habitaciones es de : $ {price:.2f}') 