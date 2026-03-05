from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "clave_super_secreta"

tareas = []  # Lista temporal en memoria

usuarios = [
    {"nombre": "Juan Carlos Pérez", "direccion": "Plaza de Armas 123", "ciudad": "La Serena", "activos": 3},
    {"nombre": "María González", "direccion": "Av. Balmaceda 450", "ciudad": "Coquimbo", "activos": 5},
    {"nombre": "Carlos Ramírez", "direccion": "Av. Francisco de Aguirre 920", "ciudad": "La Serena", "activos": 2},
    {"nombre": "Héctor Patricio Lillo Vega", "direccion": "Av. Francisco de Aguirre 789", "ciudad": "La Serena", "activos": 6}
]

#------------------------------------------------------------------------------------ 

@app.route('/')
def home():

    total = len(tareas)

    sin_empezar = sum(1 for t in tareas if t["estado"] == "sin_empezar")
    pendientes = sum(1 for t in tareas if t["estado"] == "pendiente")
    completadas = sum(1 for t in tareas if t["estado"] == "completado")

    if total > 0:
        porcentaje_sin_empezar = int((sin_empezar / total) * 100)
        porcentaje_pendientes = int((pendientes / total) * 100)
        porcentaje_completadas = int((completadas / total) * 100)
    else:
        porcentaje_sin_empezar = 0
        porcentaje_pendientes = 0
        porcentaje_completadas = 0

    return render_template(
        'home.html',
        tareas=tareas,
        total=total,
        sin_empezar=sin_empezar,
        pendientes=pendientes,
        completadas=completadas,
        porcentaje_sin_empezar=porcentaje_sin_empezar,
        porcentaje_pendientes=porcentaje_pendientes,
        porcentaje_completadas=porcentaje_completadas
    )  

#------------------------------------------------------------------------------------ 

@app.route('/about')
def about():
    return render_template("about.html", usuarios=usuarios)
    # return render_template('about.html')

#------------------------------------------------------------------------------------ 

@app.route('/ver_detalle')
def ver_detalle():
    return render_template('ver_detalle.html')

#------------------------------------------------------------------------------------ 

@app.route('/agregar', methods=['POST'])
def agregar():
    nueva_tarea = request.form.get('tarea').strip()

    if nueva_tarea != "":
        tareas.append({
            "texto": nueva_tarea,
            "estado": "sin_empezar"
        })

    return redirect(url_for('home'))

#------------------------------------------------------------------------------------ 

@app.route('/modificar/<int:indice>', methods=['POST'])
def modificar(indice):

    tarea_editada = request.form.get('tarea_editada', '').strip()
    estado = request.form.get('estado')

    if tarea_editada != "":
        tareas[indice]["texto"] = tarea_editada
        tareas[indice]["estado"] = estado

    return redirect(url_for('home'))

#------------------------------------------------------------------------------------ 

@app.route('/eliminar/<int:indice>', methods=['POST'])
def eliminar(indice):
    tareas.pop(indice)
    return redirect(url_for('home'))

#------------------------------------------------------------------------------------ 

@app.route('/eliminar_todo', methods=['POST'])
def eliminar_todo():
    global tareas
    tareas.clear()
    return redirect(url_for('home'))

#------------------------------------------------------------------------------------ 












if __name__ == '__main__':
    app.run(debug=True)



