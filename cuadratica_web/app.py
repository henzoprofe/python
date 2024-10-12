from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    # Obtenemos los valores desde el formulario
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    
    # Calculamos el discriminante
    disc = b * b - 4 * a * c
    
    # Determinamos las soluciones basadas en el discriminante
    if disc < 0:
        result = "No existe solución real. Existen dos soluciones complejas."
    elif disc == 0:
        x = -b / (2 * a)
        result = f"Existe una única solución real: x = {x}"
    else:
        x1 = (-b - disc**0.5) / (2 * a)
        x2 = (-b + disc**0.5) / (2 * a)
        result = f"Existen dos soluciones reales: x1 = {x1} y x2 = {x2}"
    
    # Redirigimos a la página de resultados
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
