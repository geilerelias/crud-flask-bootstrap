from model import db, Persona

def create_persona(nombre, telefono, sexo):
    # Crea una nueva instancia de Persona con los datos proporcionados
    new_persona = Persona(nombre=nombre, telefono=telefono, sexo=sexo)

    # Agrega el nuevo persona a la sesión de la base de datos
    db.session.add(new_persona)

    # Confirma los cambios en la base de datos
    db.session.commit()

    # Devuelve el objeto del nuevo persona creado
    return new_persona


def get_all_personas():
    return Persona.query.all()

def get_persona_by_id(persona_id):
    return Persona.query.get(persona_id)

def update_persona(persona_id, nombre, telefono, sexo):
    persona = Persona.query.get(persona_id)
    if persona:
        persona.nombre = nombre
        persona.telefono = telefono
        persona.sexo = sexo
        db.session.commit()
        return persona
    return None

def delete_persona(persona_id):
    persona = Persona.query.get(persona_id)
    if persona:
        db.session.delete(persona)
        db.session.commit()
        return True
    return False
