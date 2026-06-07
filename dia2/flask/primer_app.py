from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>Hola Mundo con Flask</h1></center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','')
    return f"<h1>Hola {nombre}</h1>"

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a,b):
    resultado = a + b
    return f"<center><h1>La suma de {a} + {b} es {resultado} </h1></center>"

#operaciones permitidas: suma, resta, multiplicacion, division
@app.route('/<operacion>/<int:num1>/<int:num2>')
def operaciones(operacion, num1, num2):
    resultado = 0
    """Dependiendo de la operación mostrar la suma, resta, multiplicación o división"""
    if operacion=="suma":
        resultado = num1 + num2
    elif operacion=="resta":
        resultado = num1 - num2
    elif operacion=="multiplicacion":
        resultado = num1 * num2
    elif operacion=="division":
        resultado = float(num1/num2)
    else:
        return f"<center><h1>Operación invalida</h1></center>"

    return f"<center><h1>La {operacion} de {num1} y {num2} es {resultado} </h1></center>"

app.run(debug=True)