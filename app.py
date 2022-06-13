from flask import Flask, render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
#CADENA DE CONEXION
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#VARIABLES DE NUESTRA APP
esquema_db = SQLAlchemy(app)
mapeo_ma = Marshmallow(app)
# CREAR MODELO DE BD
class Personas(esquema_db.Model):
    id = esquema_db.Column(esquema_db.Integer, primary_key=True)
    nombre = esquema_db.Column(esquema_db.String(45))
    direccion =  esquema_db.Column(esquema_db.String(45))

    def __init__(self,nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

# CREAR MODEL DE LA TABLA
esquema_db.create_all()

#CREAR ESQUEMA
class PersonasSchema(mapeo_ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'direccion')

# OBTENER RESPUESTAS
personas_informacion = PersonasSchema(many=True)
@app.route('/estructura')
def estructura():
    datos = Personas.query.all()
    resultado = personas_informacion.dump(datos)
    return render_template('estructura.html', resultados = resultado)

# @app.route('/estructura')
# def estructura():
#     return render_template('estructura.html')
@app.route('/conocenos')
def conocenos():
    return render_template('conocenos.html')
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')
@app.route('/ofertaeducativa')
def ofertaeducativa():
    return render_template('ofertaeducativa.html')
@app.route('/ubicacion')
def ubicacion():
    return render_template('ubicacion.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 