from flask import Flask, render_template, request, redirect, url_for, flash
from model import db
import controller,persona_controller
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    products = controller.get_all_products()
    return render_template('index.html', products=products)

@app.route('/products')    
def product_list():
    products = controller.get_all_products()
    return render_template('product_list.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = controller.get_product_by_id(product_id)
    return render_template('product_detail.html', product=product)

@app.route('/create_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        controller.create_product(nombre, descripcion, precio)
        flash('Producto creado con éxito!')
        return redirect(url_for('product_list'))
    return render_template('product_form.html')

@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = controller.get_product_by_id(product_id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        controller.update_product(product_id, nombre, descripcion, precio)
        flash('¡Producto actualizado exitosamente!')
        return redirect(url_for('product_list'))
    return render_template('product_form.html', product=product)

@app.route('/delete_product/<int:product_id>')
def delete_product(product_id):
    controller.delete_product(product_id)
    flash('Producto eliminado exitosamente!')
    return redirect(url_for('product_list'))
    
    
@app.route('/persons')    
def person_list():
    persons = persona_controller.get_all_personas()
    return render_template('person_list.html', persons=persons)
    
@app.route('/create_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        sexo = request.form['sexo']
        persona_controller.create_persona(nombre, telefono, sexo)
        flash('Persona creada con éxito!')
        return redirect(url_for('person_list'))
    return render_template('person_form.html')
    
@app.route('/person/<int:person_id>')
def person_detail(person_id):
    person = persona_controller.get_persona_by_id(person_id)
    return render_template('person_detail.html', person=person)

@app.route('/edit_person/<int:person_id>', methods=['GET', 'POST'])
def edit_person(person_id):
    person = persona_controller.get_persona_by_id(person_id)
    # Concatenar el mensaje con el nombre de la persona
    message = f'Persona id: {person.id} - nombre: {person.nombre} consultada!'
    # Enviar el mensaje a flash
    flash(message)
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        sexo = request.form['sexo']
        persona_controller.update_persona(person_id, nombre, telefono, sexo)
        flash('¡Persona actualizada exitosamente!')
        return redirect(url_for('person_list'))
    return render_template('person_form.html', person=person)

@app.route('/delete_person/<int:person_id>')
def delete_person(person_id):
    persona_controller.delete_persona(person_id)
    flash('Persona eliminado exitosamente!')
    return redirect(url_for('person_list'))
    

if __name__ == '__main__':
    app.run(debug=True)
