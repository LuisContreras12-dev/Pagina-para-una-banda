import json
import pytest
from app import app, cargar_json


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_inicio(client):
    resp = client.get('/')
    assert resp.status_code == 200
    assert 'Coldplay' in resp.data.decode('utf-8')


def test_tour(client):
    resp = client.get('/tour')
    assert resp.status_code == 200
    assert 'Foro Sol' in resp.data.decode('utf-8')


def test_discografia(client):
    resp = client.get('/discografia')
    assert resp.status_code == 200
    assert 'Parachutes' in resp.data.decode('utf-8')


def test_media(client):
    resp = client.get('/media')
    assert resp.status_code == 200
    assert 'Fotos' in resp.data.decode('utf-8')
    assert 'Videos' in resp.data.decode('utf-8')


def test_cargar_json_tour():
    datos = cargar_json('tour.json')
    assert isinstance(datos, list)
    assert len(datos) > 0
    assert 'fecha' in datos[0]


def test_cargar_json_discografia():
    datos = cargar_json('discografia.json')
    assert isinstance(datos, list)
    assert len(datos) > 0
    assert 'titulo' in datos[0]


def test_cargar_json_media():
    datos = cargar_json('media.json')
    assert isinstance(datos, list)
    fotos = [d for d in datos if d['tipo'] == 'foto']
    videos = [d for d in datos if d['tipo'] == 'video']
    assert len(fotos) > 0
    assert len(videos) > 0


def test_cargar_json_redes():
    datos = cargar_json('redes.json')
    assert isinstance(datos, list)
    assert len(datos) > 0
    assert 'url' in datos[0]


def test_footer_redes_sociales(client):
    resp = client.get('/')
    html = resp.data.decode('utf-8')
    assert 'facebook.com/coldplay' in html
    assert 'instagram.com/coldplay' in html
