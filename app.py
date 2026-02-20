import json
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = 'foo-fighters-secret-key-2026'

bootstrap = Bootstrap5(app)

# ── Directorio de datos ──────────────────────────────────────────────
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def cargar_json(nombre_archivo):
    """Carga y devuelve los datos de un archivo JSON."""
    ruta = os.path.join(DATA_DIR, nombre_archivo)
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)


# ── Rutas ─────────────────────────────────────────────────────────────
@app.route('/')
def inicio():
    """Página principal con información general de la banda."""
    return render_template('inicio.html')


@app.route('/tour')
def tour():
    """Listado de fechas del tour."""
    fechas = cargar_json('tour.json')
    return render_template('tour.html', fechas=fechas)


@app.route('/discografia')
def discografia():
    """Discografía completa de la banda."""
    albumes = cargar_json('discografia.json')
    return render_template('discografia.html', albumes=albumes)


@app.route('/media')
def media():
    """Fotos y videos de la banda."""
    contenido = cargar_json('media.json')
    fotos = [item for item in contenido if item['tipo'] == 'foto']
    videos = [item for item in contenido if item['tipo'] == 'video']
    return render_template('media.html', fotos=fotos, videos=videos)


@app.route('/redes')
def redes():
    """Redes sociales de la banda."""
    datos = cargar_json('social.json')
    return render_template('redes.html', redes=datos['redes'], banda=datos['banda'])


# ── Punto de entrada ──────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
