from flask import Flask

app = Flask(__name__)

# Aquí es donde puedes configurar tu aplicación, si es necesario
# Ejemplo: app.config['SECRET_KEY'] = 'mi_clave_secreta'

# Importa las rutas después de crear la instancia de la app
from app import routes
