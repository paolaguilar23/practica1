from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de ejemplo
servicios = [
    {"nombre": "Tortas Personalizadas", "descripcion": "Creamos tortas para cualquier ocasión.", "imagen": "torta1.jpg"},
    {"nombre": "Cupcakes", "descripcion": "Deliciosos cupcakes para todos los gustos.", "imagen": "cupcake.jpg"},
    {"nombre": "Galletas", "descripcion": "Galletas recién horneadas.", "imagen": "galleta.jpg"},
]

noticias = [
    {"titulo": "Apertura de Nueva Sucursal", "descripcion": "¡Ven a conocer nuestra nueva sucursal!", "imagen": "sucursal.jpg"},
    {"titulo": "Nuevos Productos", "descripcion": "Lanzamos nuevos sabores de cupcakes.", "imagen": "nuevos_sabores.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html', servicios=servicios, noticias=noticias)

@app.route('/quienes-somos')
def quienes_somos():
    return render_template('quienes_somos.html')

@app.route('/servicios')
def servicios_page():
    return render_template('servicios.html', servicios=servicios)

@app.route('/noticias')
def noticias_page():
    return render_template('noticias.html', noticias=noticias)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Aquí podrías manejar el envío del formulario
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        mensaje = request.form.get('mensaje')
        # Procesar los datos como desees (guardar en DB, enviar email, etc.)
        return redirect(url_for('index'))
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
