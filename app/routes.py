import os
from flask import render_template
from app import app
import markdown

@app.route('/')
def index():
    # La ruta ahora es a la raíz del proyecto
    readme_path = os.path.join(os.getcwd(), 'README.md')

    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        return "El archivo README.md no se encuentra."

    # Convertir el contenido Markdown a HTML
    html_content = markdown.markdown(readme_content)

    # Pasar el HTML generado a la plantilla
    return render_template('index.html', readme_html=html_content)
