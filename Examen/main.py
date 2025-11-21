from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        Nombre = (request.form['Nombre'])
        Edad = int(request.form['Edad'])
        Tarros = (request.form['Tarros'])
        Tarro = int(Tarros) * 9000
        descuento1 = Tarro * (15/100)
        descuento2 = Tarro * (25/100)
        total1 = Tarro - descuento1
        total2 = Tarro - descuento2
        return render_template('ejercicio1.html',
                           Nombre =Nombre,
                           Edad= Edad,
                           Tarros= Tarros,
                           Tarro= Tarro ,
                           descuento1= descuento1,
                           descuento2= descuento2,
                           total1= total1,
                           total2= total2 )
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET','POST'])
def ejercicio2():
    if request.method == 'POST':
        Nombre = (request.form['Nombre'])
        contraseña = (request.form['contraseña'])
        return render_template('ejercicio2.html', Nombre=Nombre,
                               contraseña= contraseña)
    return render_template('ejercicio2.html')

if __name__ == "__main__":
    app.run(debug=True)