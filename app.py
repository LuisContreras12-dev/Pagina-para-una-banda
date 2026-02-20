import json
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

bootstrap = Bootstrap5(app)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "band_data.json")
_band_data = None


def load_data():
    global _band_data
    if _band_data is None:
        with open(DATA_FILE, encoding="utf-8") as f:
            _band_data = json.load(f)
    return _band_data


@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", band=data["band"], tour=data["tour"][:3])


@app.route("/tour")
def tour():
    data = load_data()
    return render_template("tour.html", band=data["band"], tour=data["tour"])


@app.route("/discografia")
def discografia():
    data = load_data()
    return render_template(
        "discografia.html", band=data["band"], discography=data["discography"]
    )


@app.route("/media")
def media():
    data = load_data()
    return render_template(
        "media.html",
        band=data["band"],
        videos=data["videos"],
        photos=data["photos"],
    )


@app.route("/redes")
def redes():
    data = load_data()
    return render_template(
        "redes.html", band=data["band"], social_media=data["social_media"]
    )


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug)
