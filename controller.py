from model import db, Producto

def create_product(nombre, descripcion, precio):
    # Crea una nueva instancia de Producto con los datos proporcionados
    new_product = Producto(nombre=nombre, descripcion=descripcion, precio=precio)

    # Agrega el nuevo producto a la sesión de la base de datos
    db.session.add(new_product)

    # Confirma los cambios en la base de datos
    db.session.commit()

    # Devuelve el objeto del nuevo producto creado
    return new_product


def get_all_products():
    return Producto.query.all()

def get_product_by_id(product_id):
    return Producto.query.get(product_id)

def update_product(product_id, nombre, descripcion, precio):
    product = Producto.query.get(product_id)
    if product:
        product.nombre = nombre
        product.descripcion = descripcion
        product.precio = precio
        db.session.commit()
        return product
    return None

def delete_product(product_id):
    product = Producto.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False
