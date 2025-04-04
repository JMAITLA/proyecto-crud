# app.py
from flask import Flask, render_template, request, redirect, url_for
from modelos import db, Tarea

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    descripcion = request.form['descripcion']
    nueva_tarea = Tarea(descripcion=descripcion)
    db.session.add(nueva_tarea)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/actualizar/<int:id>')
def actualizar(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)