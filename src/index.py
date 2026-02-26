from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tareas = []  # Lista temporal en memoria


@app.route('/')
def home():
    return render_template('home.html', tareas=tareas)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/agregar', methods=['POST'])
def agregar():
    nueva_tarea = request.form.get('tarea').strip()

    if nueva_tarea != "":
        tareas.append(nueva_tarea)

    return redirect(url_for('home'))

@app.route('/eliminar/<int:indice>', methods=['POST'])
def eliminar(indice):
    tareas.pop(indice)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)



#FORMATO ANTIGUO 26/02/2026:

# from flask import Flask, render_template
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return render_template('home.html')
# @app.route('/about')
# def about():
#     return render_template('about.html')
# if __name__ == '__main__':
#     app.run(debug=True) 

