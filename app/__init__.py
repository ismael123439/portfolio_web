# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importa Flask-Migrate para gestionar migraciones

app = Flask(__name__)

# Configuración de la base de datos con MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://u9bxcc2zaznhga0u:7Ph2rd466SuMLDBU5irr@bqw84s2dmv3vcfj1puba-mysql.services.clever-cloud.com:3306/bqw84s2dmv3vcfj1puba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa SQLAlchemy y Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

try:
    # Prueba la conexión a la base de datos
    with app.app_context():
        db.engine.connect()
        print("Conexión a la base de datos exitosa.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")

# Importa los módulos necesarios para la app
from app import routes, models
