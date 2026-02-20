import json
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-secreta-desarrollo')
bootstrap = Bootstrap5(app)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def cargar_json(nombre_archivo):
    ruta = os.path.join(DATA_DIR, nombre_archivo)
    try:
        with open(ruta, encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


@app.route('/')
def inicio():
    redes = cargar_json('redes.json')
    return render_template('inicio.html', redes=redes)


@app.route('/tour')
def tour():
    fechas = cargar_json('tour.json')
    redes = cargar_json('redes.json')
    return render_template('tour.html', fechas=fechas, redes=redes)


@app.route('/discografia')
def discografia():
    albumes = cargar_json('discografia.json')
    redes = cargar_json('redes.json')
    return render_template('discografia.html', albumes=albumes, redes=redes)


@app.route('/media')
def media():
    contenido = cargar_json('media.json')
    redes = cargar_json('redes.json')
    fotos = [item for item in contenido if item['tipo'] == 'foto']
    videos = [item for item in contenido if item['tipo'] == 'video']
    return render_template('media.html', fotos=fotos, videos=videos, redes=redes)


if __name__ == '__main__':
    app.run(debug=True)
