
from flask import Flask, request

app = Flask("ejemploJunio")

@app.route('/metodo2',methods=['POST']) 
def h():
    parametroPython = str(request.form['nombre'])
    parametroPython2 = str(request.form['passwd'])
    return "1"

@app.route('/hola') 
def he():
    return "hola Mundo" 

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')